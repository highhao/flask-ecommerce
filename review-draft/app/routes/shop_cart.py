from functools import wraps
from flask import Blueprint, jsonify, redirect, render_template, request, session, url_for
from app.repositories.product_repository import ProductRepository
from app.services.cart_service import CartError, CartService

shop_cart = Blueprint("shop_cart", __name__)
cart_service = CartService(ProductRepository())


def login_checkout(route_func):
    @wraps(route_func)
    def decorated_route(*args, **kwargs):
        if not session.get("user_info", {}).get("MemberID"):
            return redirect(url_for("auth.login"))
        return route_func(*args, **kwargs)
    return decorated_route


@shop_cart.route("/add_to_cart", methods=["POST"])
def add_to_cart():
    data = request.get_json(silent=True) or {}
    product_id, quantity = data.get("product_id"), data.get("quantity")
    if not isinstance(product_id, (str, int)) or not str(product_id).isdigit() or type(quantity) is not int or not 1 <= quantity <= 10:
        return jsonify(error="商品或數量不正確"), 400
    if not cart_service.products.find_active(str(product_id)):
        return jsonify(error="商品不存在或已下架"), 404
    cart = session.get("cart", {})
    key = str(product_id)
    if cart.get(key, 0) + quantity > 10:
        return jsonify(error="單項商品最多 10 件"), 400
    cart[key] = cart.get(key, 0) + quantity
    session["cart"] = cart
    return jsonify(cart_count=sum(cart.values()))


@shop_cart.route("/update_cart", methods=["GET"])
def update_cart():
    return jsonify(cart_count=sum(session.get("cart", {}).values()))


@shop_cart.route("/delete", methods=["POST"])
def delete_item():
    cart = session.get("cart", {})
    cart.pop(request.form.get("delete_id"), None)
    session["cart"] = cart
    return redirect(url_for("shop_cart.checkout"))


@shop_cart.route("/checkout", methods=["GET"])
@login_checkout
def checkout():
    try:
        final_cart = cart_service.checkout(session.get("cart", {}))
    except CartError as exc:
        return str(exc), 400
    session["order_info"] = {"MemberId": session["user_info"]["MemberID"],
                             "TotalPrice": final_cart["total_amount"], "cart_items": final_cart["cart_items"]}
    return render_template("checkout.html", final_cart=final_cart)


@shop_cart.route("/confirm_checkout")
def confirm_checkout():
    return render_template("checkout_response.html")
