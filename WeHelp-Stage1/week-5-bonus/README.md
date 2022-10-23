### 額外練習
<br />


● 你可以自由使用任何方式設計資料庫，進一步完成以下需求：
<br />
我們不只要記錄留言按讚的數量，還要紀錄每一個留言的按讚會員是誰，支援以下使用場合：

- 可以根據留言編號取得該留言有哪些會員按讚。
- 會員若是嘗試對留言按讚：要能先檢查是否曾經按過讚，然後才將按讚的數量 +1 並且記錄按讚的會員是誰。

不用寫程式，只要你認為你的資料庫設計能充分支援以上場景即可。
<br />
<br />

>方式一
```
這是我設計出來的資料庫關聯圖，在新的message_like資料表中，
message_id和like_member_id會分別來自message與member的資料表。

同時，會有另一欄like_action欄位用來記錄此留言其會員是否已經按讚，
透過設定預設值為0，執行按讚動作後的值更改為1，來判別與檢查會員是否已讚過讚，
若為0才將按讚的數量 +1 ，並且記錄按讚的會員動作資料。
```
![message_like ERM](https://user-images.githubusercontent.com/43780809/197397491-32dd2830-cd3e-464f-89e3-eadcade4d5a7.png)
<br />
<br />

>方式二
```
如果把like_action刪除的話，流程應該會變成一開始message_like會是空白的，
當有會員進行按讚動作，才在message_like表中進行insert按讚資料。

在檢查是否已讚過讚時，只要在message_like表中找不到相對應的資料，就當作尚未按讚～
```
![message_like ERM2](https://user-images.githubusercontent.com/43780809/197397563-149e4f81-2e5a-474e-b0d1-5afd70d20a18.png)
