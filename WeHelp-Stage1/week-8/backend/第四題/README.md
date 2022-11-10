# 第四題

### 1. 了解主鍵 (Primary Key) 和索引 (Index) 的觀念。

PRIMARY Key(PK) (主鍵)：

- 是一種 index 但不能為空值(NULL)，PK 會自動建立 index
- 每個 table 只能有一個 PRIMARY Key
- 語法為 CREATETABLE tablename ( \[…], PRIMARY KEY (列的列表) );
- 在 Rails(一個用 Ruby 所寫的 Web 開發框架) 裡面，默認 id 為 primary key

Index (索引鍵)：

- 資料索引，可加快搜尋速度，Mysql 引擎除了 Archive 外都支援 B-tree 索引
- 可多欄位設定為 Index
- 語法為 CREATE INDEX <索引的名字> ON tablename (列的列表)

<br />

> 相關關鍵字：

#### PRIMARY Key(PK), 主鍵, Index, 索引鍵

> 參考資源：

- [[SQL 基本觀念] primary Key / Index / Unique 差別](https://blog.niclin.tw/2018/06/09/sql-基本觀念-primary-key-/-index-/-unique-差別/)
- [麥克的學習紀錄](https://miggo.pixnet.net/blog/post/30862194-%5Bmysql基本觀念%5D-primary-key---index---unique差別)
- [Rails 起步走 — Ruby on Rails 指南](https://rails.ruby.tw/getting_started.html)

<hr >

### 2. 請在 member 資料表中加入適當的索引，加快以下 SQL 語句的查詢效率 SELECT \* FROM member WHERE username=’test’ and password=’test’

建立兩個新資料表 username、password，並個別將 username_id 與 password_id 設定為主鍵欄位。
同時，以分別設定外鍵與 member_id 相互連結。

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
