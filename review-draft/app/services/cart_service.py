from decimal import Decimal


class CartError(ValueError):
    pass


class CartService:
    def __init__(self, products):
        self.products = products

    def checkout(self, cart):
        if not cart:
            raise CartError("購物車是空的")
        items = []
        total = Decimal("0")
        for product_id, quantity in cart.items():
            if type(quantity) is not int or not 1 <= quantity <= 10:
                raise CartError("商品數量不正確")
            product = self.products.find_active(product_id)
            if not product:
                raise CartError("商品不存在或已下架")
            if product["Stock"] < quantity:
                raise CartError("商品庫存不足")
            price = Decimal(str(product["Price"]))
            subtotal = price * quantity
            total += subtotal
            items.append({"product_id": product_id, "product_name": product["ProductName"],
                          "price": float(price), "quantity": quantity, "subtotal": float(subtotal)})
        if total != total.to_integral_value():
            raise CartError("付款金額必須為整數")
        return {"cart_items": items, "total_amount": int(total)}
