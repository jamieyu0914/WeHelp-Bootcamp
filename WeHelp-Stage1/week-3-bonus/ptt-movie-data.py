#抓取 PTT 電影版 每一篇文章的標題
from array import array
from itertools import count
from unittest import result
import urllib.request as req

# 建立或清空輸出的 txt 檔案
with open('movie.txt', 'w') as txtfile:
    txtfile.write('')

# 爬取[好雷]
def getdata_good(url):
    # 建立 request 物件，附加 request headers 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") #取得的資料是 json 格式

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") #尋找所有class="title"的div標籤
    
    for title in titles:
        if title.a != None: #去除本文已被刪除的資訊(不含a標籤)
            re = title.a.string.find("Re:")
            if re == -1: 
                good = title.a.string.find("[好雷]")
                if good != -1:
                    datalist_good = title.a.string
                    # 開啟輸出的 txt 檔案
                    with open('movie.txt', 'a') as txtfile:
                    # 建立 txt 檔寫入器
                        txtfile.write(datalist_good+'\n')

    nextlink = root.find("a", string="‹ 上頁") #找到上頁標籤
    #print("DONE 1") 
    return (nextlink["href"]) 

# 爬取[普雷]
def getdata_normal(url):
    # 建立 request 物件，附加 request headers 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") #取得的資料是 json 格式

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") #尋找所有class="title"的div標籤
    
    for title in titles:
        if title.a != None: #去除本文已被刪除的資訊(不含a標籤)
            re = title.a.string.find("Re:")
            if re == -1: 
                normal = title.a.string.find("[普雷]")
                if normal != -1:
                    datalist_normal = title.a.string
                    # 開啟輸出的 txt 檔案
                    with open('movie.txt', 'a') as txtfile:
                    # 建立 txt 檔寫入器
                        txtfile.write(datalist_normal+'\n')

    nextlink = root.find("a", string="‹ 上頁") #找到上頁標籤
    #print("DONE 2")
    return (nextlink["href"])

# 爬取[負雷]
def getdata_bad(url):
    # 建立 request 物件，附加 request headers 的資訊
    request = req.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Safari/605.1.15"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8") #取得的資料是 json 格式

    import bs4
    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="title") #尋找所有class="title"的div標籤

    for title in titles:
        if title.a != None: #去除本文已被刪除的資訊(不含a標籤)
            re = title.a.string.find("Re:")
            if re == -1: 
                bad = title.a.string.find("[負雷]")
                if bad != -1:
                    datalist_bad = title.a.string
                    # 開啟輸出的 txt 檔案
                    with open('movie.txt', 'a') as txtfile:
                    # 建立 txt 檔寫入器
                        txtfile.write(datalist_bad+'\n')                         

    nextlink = root.find("a", string="‹ 上頁") #找到上頁標籤
    #print("DONE 3")
    return (nextlink["href"])    

#抓取一個頁面的[好雷]標題
pageurl = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count<10:
    pageurl = "https://www.ptt.cc"+getdata_good(pageurl)
    count+=1

#抓取一個頁面的[普雷]標題
pageurl = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count<10:
    pageurl = "https://www.ptt.cc"+getdata_normal(pageurl)
    count+=1

#抓取一個頁面的[負雷]標題
pageurl = "https://www.ptt.cc/bbs/movie/index.html"
count = 0
while count<10:
    pageurl = "https://www.ptt.cc"+getdata_bad(pageurl)
    count+=1

print("DONE!")

        


    





