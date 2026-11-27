# 電商分層改造｜審閱草稿

這是依原始 Flask 電商 demo 整理的部分程式，供審閱分層使用，並非完整可執行專案。

- `app/routes/shop_cart.py`：HTTP 請求及 Session。
- `app/services/cart_service.py`：購物車計算及輸入檢查。
- `app/repositories/product_repository.py`：商品查詢。
- `database.py`：連線與交易資源管理。
- `app/routes/ECPay.py`、`app/integrations/ecpay_signature.py`：付款流程與檢查碼處理的整理中版本。

目前未包含完整設定、資料庫建表、頁面及所有依賴。付款訂單、庫存一致性、重複回呼、CSRF 與整體流程尚未完成或驗證，請勿用於真實交易。購物車計算和連線關閉曾以模擬物件做局部檢查；尚未進行資料庫與金流端到端測試。
