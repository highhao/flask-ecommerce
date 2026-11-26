# 購物與結帳流程

```mermaid
flowchart LR
    Browse[瀏覽商品] --> Cart[加入 Session 購物車]
    Cart --> Login[登入與庫存檢查]
    Login --> Checkout[整理結帳資料]
    Checkout --> Page[顯示結帳確認頁]
```

程式包含結帳確認頁；訂單寫入與扣庫存程式段落目前為註解。
