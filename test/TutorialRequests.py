import requests
url = 'https://www.google.com' #先將欲發出 GET 請求的網址先存在 url

res = requests.get(url) #對 url 發出 GET 請求，並將 Response 包成回傳物件存在 res
print(type(res), res) #Output: <class 'requests.models.Response'> <Response [200]>




import requests
import json #JSON 非 python 原生型態但為內建，因此直接引入即可

# 使用字典傳入 POST 參數
data = {'account':'testOwO', 'password':'testOwO'}
url = 'https://zh.wikipedia.org/'
print(requests.post(url, data=data)) #Output: <Response [200]>

#使用 JSON 傳入 POST 參數
data = json.dumps(data)
url = 'https://zh.wikipedia.org/'
print(requests.post(url, data=data)) #Output: <Response [200]>