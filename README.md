# Flask 電商網站

提供商品瀏覽、會員驗證、Session 購物車與結帳資料整理。

## 購物與結帳流程

```mermaid
flowchart TB
    A[瀏覽商品] --> B[查看商品資訊]
    B --> C[加入 Session 購物車]
    C --> D[登入並檢查價格與庫存]
    D --> E[整理結帳資料]
    E --> F[顯示結帳確認頁]
```

## 架構心智圖

```mermaid
mindmap
  root((Flask 電商))
    Application
      App Factory
      設定與擴充初始化
    功能路由
      商品 Blueprint
      會員 Blueprint
      購物車 Blueprint
    資料與頁面
      MySQL Database helper
      Jinja2 Templates
    外部整合
      OAuth
      SMTP
      ECPay
      Socket.IO
```

## 設計與技術

- **分層方式：** App Factory 負責組裝應用；Blueprint 依商品、會員與購物車拆分路由；Database helper 封裝 MySQL 存取。
- **技術：** Python 3.11、Flask 3、MySQL、Jinja2、Flask-SocketIO、OAuth、ECPay。
- **實作範圍：** 訂單寫入與扣庫存程式段落目前為註解；流程圖止於結帳確認頁。
