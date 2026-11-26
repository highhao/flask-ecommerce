# Flask 電商網站

**技術：** Python 3.11、Flask 3、MySQL、Jinja2、Flask-SocketIO、OAuth、ECPay。

## 專案情境

提供商品瀏覽、會員驗證、Session 購物車及結帳資料整理，並整合 OAuth、SMTP 與 ECPay。現有程式中的訂單寫入與扣庫存段落為註解。

## 架構摘要

App Factory 載入設定並註冊 Blueprints；路由依商品、會員與購物車拆分，資料由 MySQL 存取，頁面由 Jinja2 呈現。

## 架構與流程

- [系統架構與模組責任](docs/architecture.md)
- [購物與結帳流程](docs/workflow.md)

## 後續優化建議

先完成訂單持久化與交易內的價格／庫存確認，再為付款回呼加入簽章驗證、狀態檢查與冪等處理。

**English:** A Flask e-commerce application with product browsing, authentication, session cart, and checkout preparation.
