# Flask 電商網站

**技術：** Python 3.11、Flask 3、MySQL、Jinja2、Flask-SocketIO、OAuth、ECPay。

## 專案定位

涵蓋商品瀏覽、會員驗證、Session 購物車與結帳資料整理，並整合 OAuth、SMTP 與 ECPay。現有程式的訂單寫入與扣庫存段落為註解。

## 架構重點

App Factory 載入設定並註冊 Blueprints；路由依商品、會員與購物車功能拆分，資料由 MySQL 存取，頁面由 Jinja2 呈現。

## 詳細文件

- [系統架構與模組責任](docs/architecture.md)
- [購物與結帳流程](docs/workflow.md)

## 後續優化方向（設計建議）

- 先完成訂單持久化，在資料庫交易內重新確認價格與庫存，再建立訂單並扣減庫存。
- 付款回呼加入簽章驗證、狀態檢查與冪等處理。

English: A Flask e-commerce application with product browsing, authentication, session cart, and checkout preparation.
