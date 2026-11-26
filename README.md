# Flask 電商網站

提供商品瀏覽、會員驗證、Session 購物車與結帳資料整理。

## 技術

Python 3.11、Flask 3、MySQL、Jinja2、Flask-SocketIO、OAuth、ECPay。

## 架構

- **App Factory：** 載入設定、初始化擴充並註冊 Blueprint。
- **Blueprint：** 依商品、會員與購物車拆分路由。
- **資料與頁面：** Database helper 存取 MySQL，Jinja2 呈現頁面。
- **外部整合：** OAuth、SMTP、ECPay 與 Socket.IO。

## 購物與結帳流程

1. 瀏覽商品並查看商品資訊。
2. 將商品加入 Session 購物車。
3. 登入後檢查商品價格與庫存。
4. 整理結帳資料並顯示確認頁。

**實作範圍：** 訂單寫入與扣庫存程式段落目前為註解。

## English

A Flask e-commerce application for product browsing, authentication, session cart, and checkout preparation.
