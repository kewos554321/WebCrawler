import requests

# 2-2 post請求
url = 'https://httpbin.org/post'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

data = {
    'account': 'Jay',
    'password': '12345'
}

response = requests.post(url=url, data=data, headers=headers)
print(response.text)
# 參數用data傳遞 
# 問號可加可不加 

