# 第三題

### 1. 什麼是 CORS?

簡單地說，跨來源資源分享 CORS (Cross-Origin Resource Sharing) 是針對不同源的請求而定的規範，透過 JavaScript 存取非同源資源時，server 必須明確告知瀏覽器允許何種請求，只有 server 允許的請求能夠被瀏覽器實際發送，否則會失敗。

需要注意的是，用 JavaScript 透過 fetch API 或 XMLHttpRequest 等方式發起 request，必須遵守同源政策 (same-origin policy)。

什麼是同源政策呢？就是使用 JavaScript 存取資源時，如果是同源的情況下，存取不會受到限制；然而，在同源政策下，非同源的 request 則會因為安全性的考量受到限制。瀏覽器會強制你遵守 CORS (Cross-Origin Resource Sharing，跨域資源存取) 的規範，否則瀏覽器會讓 request 失敗。

而所謂的同源，必須滿足以下三個條件：相同的通訊協定 (protocol)，即 http/https ; 相同的網域 (domain) ; 相同的通訊埠 (port)。

如果在不是同源的情況下，就會產生一個跨來源 http 請求（cross-origin http request）。而跨來源請求必須遵守 CORS 的規範。當伺服器沒有正確設定時，請求就會因為違反 CORS 失敗，在 Chrome DevTool 就會看到以下的經典錯誤：

```
Access to fetch at *** from origin *** has been blocked by CORS policy: No 'Access-Control-Allow-Origin' header is present on the requested resource. If an opaque response serves your needs, set the request's mode to 'no-cors' to fetch the resource with CORS disabled.
```

<br />

> 相關關鍵字：

#### 跨來源 HTTP 請求, XMLHttpRequest, Fetch, 同源政策(same-origin policy), AJAX, Promise

> 參考資源：

- [AJAX 網路連線實務 - Front End 網頁前端工程教學](https://www.youtube.com/watch?v=6X8sDGFGRss&t=938s)
- [什麼是 Ajax？ 搞懂非同步請求 (Async request) 概念](https://tw.alphacamp.co/blog/ajax-asynchronous-request)
- [從 XHR 到 Fetch](https://www.ithome.com.tw/voice/121435)
- [用淺顯方式說明 Javascript 的 Promise](https://ithelp.ithome.com.tw/articles/10230214)
- [Promise - JavaScript - MDN Web Docs](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript/Reference/Global_Objects/Promise)
- [跨來源資源共用（CORS)](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/CORS)
- [[教學] CORS 是什麼? 如何設定 CORS?](https://shubo.io/what-is-cors/#什麼是-cors-cross-origin-resource-sharing)
- [使用跨來源資源分享 (CORS) -AWS](https://docs.aws.amazon.com/zh_tw/AmazonS3/latest/userguide/cors.html)

<hr >

### 2. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到 https://www.google.com/ 並取得回應嗎?

不行，因為使用 fetch() 或是 XMLHttpRequest 連結到 https://www.google.com/ ，跨來源請求資源時，CORS 規範會造成瀏覽器阻擋取得回應。

<hr >

### 3. 我們可以在自己的網頁中，使用 fetch() 或是 XMLHttpRequest 連結到https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 並取得回應嗎?和上述的狀況，差別在哪裡?

可以，請參考下方第一階段 week-3 的 index.html 練習內容。與上述連結到 https://www.google.com/ 主要差別的差別是，https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json 的網頁後端程式提供了相對應的 CORS header 設置 - Access-Control-Allow-Origin: \*，允許任何的網址都可以跨網域使用此資源，使 fetch()能夠成功取得回應物件。

![Access-Control-Allow-Origin](https://github.com/jamieyu0914/WeHelp-Bootcamp/blob/main/WeHelp-Stage1/week-8/backend/第三題/Access-Control-Allow-Origin.png)

```html
<script>
  // 利用 fetch 進行連線並取得資料{
  fetch(
    "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
  )
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      let posts = data["result"]["results"];
      //...以下省略
    });
</script>
```

<hr >

### 4. 如何開放我們自己開發的 API，讓別的網站透過 fecth() 或是 XMLHttpRequest 連結，達到如同第 3 點的可能性。

在自己開發的 API 中，若要在瀏覽器上允許跨來源存取 API 資料，就要給予相對應的通行證，新的 http header，才能達到如同第 3 點的可能性。

**根據不同的需求，需要不同的通行證，後端要怎麼設定哪些通行證呢？有哪些通行證呢？**
<br />
<br />

- Access-Control-Allow-Origin:
  允許哪些網址可以跨網域使用此資源。 Eg. http://web.com.tw 或 給\*允許所有來源可以跨域存取。<br />
  ex. Access-Control-Allow-Origin: \_<br />
  <br />
- Access-Control-Allow-Credentials：
  當前端 API request 需要帶 cookies 時，就須此屬性並將值設定為 true，預設為 false。另外，當此屬性設定為 true 時，Access-Control-Allow-Origin 則不能設定為\*<br />
  ex. Access-Control-Allow-Credentials:true<br />
  <br />
- Access-Control-Allow-Methods：支援的 Method 有哪些(POST, GET, PUT, DELETE...)
  ex. Access-Control-Allow-Methods:POST, GET, PUT, DELETE<br />
  <br />
- Access-Control-Allow-Headers：
  允許哪些自定義的 header<br />
  ex. Access-Control-Allow-Headers: Authorization<br />
  <br />
- Access-Control-Max-Age：
  preflight request 的資訊（包含 Access-Control-Allow-Methods 和 Access-Control-Allow-Headers 可以 cache 的秒數上限(單位：秒)。每一個瀏覽器會有預設的最大值 ，當 Access-Control-Max-Age 大於預設值時，會優先採用預設值。<br />
  ex. Access-Control-Max-Age: 600 // Cache results of a preflight request for 10 minutes<br />
  <br />
- Access-Control-Expose-Headers：表示 API Server 允許瀏覽器存取 response header 的白名單
  ex. Access-Control-Expose-Headers:X-My-Custom-Header -> 表示瀏覽器能夠存取 response 當中的 X-My-Custom-Header

> 參考資源：

- [DAY06 - API 串接常見問題 - CORS - 解決 CORS 問題篇](https://ithelp.ithome.com.tw/m/articles/10268821)
