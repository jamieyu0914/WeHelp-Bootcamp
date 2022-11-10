# 第五題

### 1. 什麼是 Connection Pool?能帶給我們什麼好處?為什麼?

覺得 Connection Pooling 圖示定義清楚的一張圖：
![Connection Pooling](https://i.imgur.com/VI2AbSo.png)
<br />

透過 mysql.connector 的 Connection Pool 工具連線資料庫主要有兩大好處： <br /> 1.可以使資料庫持續保持連線(pooling 的狀態)，經由預建及保留連線減少 TCP 連線關閉的成本 <br /> 2.可以限制連線數量(connection_pool.pool_size)，並預防資料庫大量連線時影響服務

> 相關關鍵字：

#### Connection Pool, 預建連線, 保留連線, TCP 連線, 限制連線數量, 預防大量連線

> 參考資源：

- [Day 30. 資料庫類型介紹與索引建立](https://ithelp.ithome.com.tw/articles/10227628)

<hr >

### 2. 如何使用官方提供的 mysql-connector-python 套件，建立 Connection Pool。

在官方的提供的 MySQL Connector/Python Developer Guide 文件中有一項目是 Connector/Python Connection Establishment， <br />
而文件中又在 Connector/Python Connection Arguments 的章節裡頭提及了 Connection Pooling。 <br />
並在章節 9.1 Connector/Python Connection Pooling 中詳細說明了相關支援的套件。 <br />

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

> 參考資源：

- [MySQL Connector/Python Developer Guide](https://dev.mysql.com/doc/connector-python/en/)
- [Chapter 7 Connector/Python Connection Establishment](https://dev.mysql.com/doc/connector-python/en/connector-python-connecting.html)
- [7.1 Connector/Python Connection Arguments](https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html)
- [9.1 Connector/Python Connection Pooling](https://dev.mysql.com/doc/connector-python/en/connector-python-connection-pooling.html)
- [10.3 pooling.MySQLConnectionPool Class](https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlconnectionpool.html)

<hr >

### 3. 需要從資料庫取得查詢資料時，如何從 Connection Pool 取得 Connection，並且在資料操作結束後，歸還 Connection 到 Connetion Pool 中。請展示你完成上述標準操作的程式碼。

首先，會透過 from mysql.connector import pooling 導入 Connection Pool 套件，並由 pooling.MySQLConnectionPool()帶入資料庫連線時所需的基本資訊，再經由 connection_pool.get_connection()從 Connection Pool 取得 Connection，呼叫資料指標(cursor)讀出資料，並在資料操作結束後，關閉資料指標(cursor)，且歸還 Connection 到 Connetion Pool 中。

請參考以下 第一階段 week-7 的 app.py 練習內容。

```python
from flask import Flask
from flask import request
from flask import Response
from flask import redirect
from flask import render_template
from flask import session
from flask import jsonify
from mysql.connector import Error
from mysql.connector import pooling
import json


connection_pool = pooling.MySQLConnectionPool(pool_name="my_connection_pool",
                                                pool_size=5,
                                                pool_reset_session=True,
                                                host='localhost',
                                                database='member',
                                                user='root',
                                                password='******') #Connection Pool



app=Flask(
    __name__,
    static_folder="public",
    static_url_path="/")
app.secret_key="any string but secret"
@app.route("/signup", methods=["POST"])
def signup():
    name = request.form["name"]
    username = request.form["username"]
    password = request.form["password"]
    if(name =="" or username == "" or password == ""):
        return redirect('/error?message=請輸入帳號、密碼')
    sql = "SELECT username FROM member_list WHERE username=%s" #SQL指令 檢查是否有重複的帳號 (username)
    val = (username,)
    try:
        # Get connection object from a pool
        connection_object = connection_pool.get_connection() #從 Connection Pool 取得 Connection
        cursor = connection_object.cursor()
        print("MySQL connection is opened")
        cursor.execute(sql, val)
        myresult = cursor.fetchall()
        x=""
        for x in myresult:
            print(x)
    except Error as e:
        print("Error while connecting to MySQL using Connection pool ", e)
    finally:
        # closing database connection.
        cursor.close()
        connection_object.close() #歸還 Connection 到 Connetion Pool 中
    print("MySQL connection is closed")
    #以下省略
```

> 參考資源：

- [寫給新手的 Cursor 小筆記 - 程式宅急便](http://kyleap.blogspot.com/2013/12/ms-sqlcursor.html)
- [Python — MySQL](https://medium.com/jeasee隨筆/python-mysql-acd7a9679109)
