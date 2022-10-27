### 資料庫關聯圖
<br />
<br />

>圖一
```
在message_list資料表中，member_id會作為外鍵與member_list資料表相互關聯。

當網頁需要從資料庫中，向資料庫取得所有留言內容時，則透過message_list.member_id=member_list.id進行合併查詢(join)。
```
<br />
<br />
<img width="407" alt="截圖 2022-10-27 下午9 23 33" src="https://user-images.githubusercontent.com/43780809/198296553-0d7bf0cd-dc09-4c18-8a72-464b827a9b44.png">
<br />
<br />
