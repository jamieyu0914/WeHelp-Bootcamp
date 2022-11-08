# 第三題

### 1. 什麼是 CORS?

簡單地說，跨來源資源分享 CORS (Cross-Origin Resource Sharing) 是針對不同源的請求而定的規範，透過 JavaScript 存取非同源資源時，server 必須明確告知瀏覽器允許何種請求，只有 server 允許的請求能夠被瀏覽器實際發送，否則會失敗。

需要注意的是，用 JavaScript 透過 fetch API 或 XMLHttpRequest 等方式發起 request，必須遵守同源政策 (same-origin policy)。

什麼是同源政策呢？簡單地說，用 JavaScript 存取資源時，如果是同源的情況下，存取不會受到限制；然而，在同源政策下，非同源的 request 則會因為安全性的考量受到限制。瀏覽器會強制你遵守 CORS (Cross-Origin Resource Sharing，跨域資源存取) 的規範，否則瀏覽器會讓 request 失敗。

而所謂的同源，必須滿足以下三個條件：相同的通訊協定 (protocol)，即 http/https ; 相同的網域 (domain) ; 相同的通訊埠 (port)。

而不是同源的情況下，就會產生一個跨來源 http 請求（cross-origin http request）。而跨來源請求必須遵守 CORS 的規範。當伺服器沒有正確設定時，請求就會因為違反 CORS 失敗，在 Chrome DevTool 就會看到以下的經典錯誤：
`Access to fetch at *** from origin *** has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.`

> 相關關鍵字：

#### 跨來源 HTTP 請求, XMLHttpRequest, Fetch, 同源政策(same-origin policy)

> 參考資源：

- [跨來源資源共用（CORS](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS)
- [[教學] CORS 是什麼? 如何設定 CORS?](https://shubo.io/what-is-cors/#什麼是-cors-cross-origin-resource-sharing)
- [使用跨來源資源分享 (CORS) -AWS](https://docs.aws.amazon.com/zh_tw/AmazonS3/latest/userguide/cors.html)

<hr >

2. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到 https://www.google.com/ 並取得回應嗎?

<hr >

### 3. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 並取得回應嗎?和上述的狀況，差別在哪裡?

可以，請參考第一階段 week-3 的 index.html

<hr >

4. 如何開放我們自己開發的 API，讓別的網站透過 fecth() 或是 XMLHttpRequest 連結，達到如同第 3 點的可能性。
