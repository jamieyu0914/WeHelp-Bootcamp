#抓取 台北市政府提供景點公開資料 
from array import array
from itertools import count
from unittest import result
import urllib.request as req
url="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
# 建立 request 物件，附加 request headers 的資訊
request=req.Request(url, headers={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #取得的資料是 json 格式




# 解析 json 格式資料，取得景點名稱
import json
data=json.loads(data)
# 取得 json 格式資料的結果
posts=data["result"]["results"]
nums = (len(posts)) #取得資料數量
array=[]
for i in range(0,nums):
    post=posts[i]
    year=post["xpostDate"].split('/',1) #分隔取出年份
    if(int(year[0])>=2015):
        #print(str(post["stitle"])) #景點名稱
        address = post["address"] #從地址中
        district = address[5:8] #取出區域位置名稱
        file = post["file"] #從檔案連結中
        #print(file)
        if(file.find('.jpg')): #尋找副檔名為.jpg結尾的連結
            a = post["file"].split("jpg")[0] #分隔後將第一張圖片連結存入 a 陣列
            firstfile = a+"jpg"
            if(a.find('.JPG')>0): #尋找尚有多個副檔名為.JPG結尾的連結
                b = post["file"].split('.JPG')[0] #分隔後將第一張圖片連結存入 b 陣列
                firstfile = b+".JPG" 
        datalist = [str(post["stitle"]),str(district),str(post["longitude"]),str(post["latitude"]),str(firstfile)]
        array.append(datalist)     

import csv
# 開啟輸出的 CSV 檔案
with open('output.csv', 'w', newline='') as csvfile:
# 建立 CSV 檔寫入器
    writer = csv.writer(csvfile)
    writer.writerows(array)# 寫入一列資料
    
