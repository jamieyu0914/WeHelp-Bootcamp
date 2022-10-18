### 要求三:SQL CRUD
<br />


● 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料。<br />
```mysql
INSERT INTO member (id, name, username, password, follower_count)
    VALUES ('1','Test','test','test','2021');
INSERT INTO member (id, name, username, password, follower_count)
    VALUES ('2','Apple','apple','apple','2022');
INSERT INTO member (id, name, username, password, follower_count)
    VALUES ('3','Banana','banana','banana','2023');
INSERT INTO member (id, name, username, password, follower_count)
    VALUES ('4','Lemon','lemon','lemon','2024');
INSERT INTO member (id, name, username, password, follower_count)
    VALUES ('5','Orange','orange','orange','2025');
```
<img width="521" alt="截圖 2022-10-19 上午4 51 47" src="https://user-images.githubusercontent.com/43780809/196542393-ee1ffa25-8008-4491-bfe0-6148f01b484d.png">
<br />


● 使用 SELECT 指令取得所有在 member 資料表中的會員資料。<br />
```mysql
SELECT * FROM member;
```
<img width="549" alt="截圖 2022-10-19 上午4 33 59" src="https://user-images.githubusercontent.com/43780809/196538305-e2100b49-ae49-4615-aaa3-fad07cbaaf14.png">
<br />


● 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序。<br />
```mysql
SELECT * FROM member ORDER BY time DESC;
```
<img width="549" alt="截圖 2022-10-19 上午4 35 05" src="https://user-images.githubusercontent.com/43780809/196539833-3e417672-97fb-432d-bba2-65cbba0d8ab2.png">
<br />


● 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )<br />
```mysql
select * from member order by time DESC limit 3 offset 1;
```
<img width="552" alt="截圖 2022-10-19 上午4 38 38" src="https://user-images.githubusercontent.com/43780809/196540029-cf1ddd67-c5c2-455f-a346-b9222cadd6ed.png">
<br />


● 使用 SELECT 指令取得欄位 username 是 test 的會員資料。<br />
```mysql
SELECT * FROM member WHERE username='test';
```
<img width="538" alt="截圖 2022-10-19 上午4 39 53" src="https://user-images.githubusercontent.com/43780809/196542714-8ebee302-b911-4c70-9707-7e298aa0c4e2.png">
<br />


● 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料。<br />
```mysql
SELECT * FROM member WHERE username='test' and password='test';
```
<img width="535" alt="截圖 2022-10-19 上午4 41 01" src="https://user-images.githubusercontent.com/43780809/196540457-55f697e8-c6b2-4103-a69b-8c02f69d6685.png">
<br />


● 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2。<br />
```mysql
UPDATE member SET name='test2' WHERE username='test';
```
<img width="542" alt="截圖 2022-10-19 上午4 42 26" src="https://user-images.githubusercontent.com/43780809/196540668-e029f337-9eaa-4e2e-83e2-7f4444aba0c1.png">
<br />


<hr />
<br />

### 要求四:SQL Aggregate Functions
<br />


● 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )。<br />
```mysql
SELECT COUNT(id) FROM member;
```
<img width="181" alt="截圖 2022-10-19 上午4 44 28" src="https://user-images.githubusercontent.com/43780809/196540987-9ef6b797-0aa2-4d18-be63-52060a58a434.png">
<br />


● 取得 member 資料表中，所有會員 follower_count 欄位的總和。<br />
```mysql
SELECT SUM(follower_count) FROM member;
```
<img width="243" alt="截圖 2022-10-19 上午4 47 00" src="https://user-images.githubusercontent.com/43780809/196541518-dc69e112-eb2c-4323-82f9-e1584df87d51.png">
<br />


● 取得 member 資料表中，所有會員 follower_count 欄位的平均數。<br />
```mysql
SELECT AVG(follower_count) FROM member;
```
<img width="251" alt="截圖 2022-10-19 上午4 45 38" src="https://user-images.githubusercontent.com/43780809/196541550-9f74a296-c7fe-4a77-afd0-0cfa5c075cf3.png">
<br />

