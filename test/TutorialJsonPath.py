import requests
import json #JSON 非 python 原生型態但為內建，因此直接引入即可

# 使用字典傳入 POST 參數
data = {'account':'testOwO', 'password':'testOwO'}
url = 'https://zh.wikipedia.org/'
print(requests.post(url, data=data)) #Output: <Response [200]>

#使用 JSON 傳入 POST 參數
data = json.dumps(data)
url = 'https://zh.wikipedia.org/'
print(requests.post(url, data=datad)) #Output: <Response [200]>


# https://twitter.com/home?lang=zh-tw