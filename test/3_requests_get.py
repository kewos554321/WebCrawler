import requests

# 2-1 get請求
# https://www.rakuya.com.tw/sell/result?city=14&zipcode=741&usecode=1
url = 'https://www.rakuya.com.tw/sell/result?'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

params = {
    'city': '14',
    'zipcode': '741',
    'usecode': '1'
}

response = requests.get(url=url, params=params, headers=headers)
print(response.text)
# 參數用param傳遞 
# 問號可加可不加

# 2-2 模擬auth驗證
# url = 'https://httpbin.org/basic-auth/Jay/12345'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }

# response = requests.get(url=url, headers=headers)
# print(response.status_code)

# response = requests.get(url=url, auth=('Jay', '12345'), headers=headers)
# print(response.status_code)

# 2-3 模擬timeout，timeout=5 等待5秒
# url = 'https://httpbin.org/delay/5'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }

# response = requests.get(url=url, headers=headers, timeout=3)
# print(response.status_code)