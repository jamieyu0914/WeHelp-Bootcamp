# 第五題

### 1. 什麼是 Connection Pool?能帶給我們什麼好處?為什麼?

覺得 Connection Pooling 圖示定義清楚的一張圖：
![Connection Pooling](https://i.imgur.com/VI2AbSo.png)
<br />

而透過 mysql.connector 的 Connection Pool 工具連線資料庫主要有兩大好處： 1.可以使資料庫持續保持連線(pooling 的狀態)，經由預建及保留連線減少 TCP 連線關閉的成本 2.可以限制連線數量(connection_pool.pool_size)，並預防資料庫大量連線時影響服務

> 相關關鍵字：

#### Connection Pool, 預建連線, 保留連線, TCP 連線, 限制連線數量, 預防大量連線

> 參考資源：

- [Day 30. 資料庫類型介紹與索引建立](https://ithelp.ithome.com.tw/articles/10227628)

<hr >

### 2. 如何使用官方提供的 mysql-connector-python 套件，建立 Connection Pool。

在官方的提供的 MySQL Connector/Python Developer Guide 文件中有一項目是 Connector/Python Connection Establishment，
而文件中又在 Connector/Python Connection Arguments 的章節裡頭提及了 Connection Pooling。
並在章節 9.1 Connector/Python Connection Pooling 中詳細說明了相關支援的套件。

其中建立 Connection Pool，請參考以下範例-
**To create a connection pool explicitly**: Create a **_MySQLConnectionPool_** object

```python
dbconfig = {
  "database": "test",
  "user":     "joe"
}

cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name = "mypool",
                                                      pool_size = 3,
                                                      **dbconfig)
```

<hr >

### 3. 如何驗證查詢效率是否真的變更好了?

可以透過使用 show profiles 來分析當前會話中語句執行的資源消耗情況，進行 SQL 的調優測量。

> 參考資源：

- [「MySQL 系列」分析 Sql 執行時間及查詢執行計劃(附資料庫和一千萬資料)](https://www.gushiciku.cn/pl/gmGu/zh-tw)

<hr >

### 4. 為什麼索引的設置能有效地改善查詢效率?

索引的最大作用就是加快查詢速度，它能從根本上減少需要掃表的記錄/行的數量。
能夠有效地化解資料表中的千萬條記錄，資料庫每一條都要檢查的難題。
也就是避免就是所謂的“全表掃描”（full table scan）。

> 參考資源：

- [索引到底能提升多少查询效率？何时该使用索引？一文快速搞懂数据库索引及合理使用它](https://bbs.huaweicloud.com/blogs/303909)
