# 第三題

### 1. 什麼是 CORS?

簡單地說，跨來源資源分享 CORS (Cross-Origin Resource Sharing) 是針對不同源的請求而定的規範，透過 JavaScript 存取非同源資源時，server 必須明確告知瀏覽器允許何種請求，只有 server 允許的請求能夠被瀏覽器實際發送，否則會失敗。

> 相關關鍵字：

#### 跨來源 HTTP 請求, XMLHttpRequest, Fetch, 同源政策(same-origin policy)

> 參考資源：

- [使用跨來源資源分享 (CORS) -AWS](https://docs.aws.amazon.com/zh_tw/AmazonS3/latest/userguide/cors.html)
- [[教學] CORS 是什麼? 如何設定 CORS?](https://shubo.io/what-is-cors/#什麼是-cors-cross-origin-resource-sharing)
- [跨來源資源共用（CORS](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS)

<hr >

2. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到 https://www.google.com/ 並取得回應嗎?

<hr >

3. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 並取得回應嗎?和上述的狀況，差別在哪裡?

可以，請參考第一階段 week-3 的 index.html

<hr >

4. 如何開放我們自己開發的 API，讓別的網站透過 fecth() 或是 XMLHttpRequest 連結，達到如同第 3 點的可能性。
