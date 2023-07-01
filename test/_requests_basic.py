import requests

# 0-0 
# official-doc: https://requests.readthedocs.io/en/latest/
# official-doc-Quickstart: https://requests.readthedocs.io/en/latest/user/quickstart/

# 1-1 response有1個類型及6種屬性
url = 'https://www.w3schools.com/python/default.asp' 
response = requests.get(url)
# print('1: ', response)
# print('2: ', type(response))

# r.text: 返回網頁HTML原始碼
# r.encoding: 返回目前網頁編碼方式，可以透過設置編碼格式(通常使用萬國碼utf-8)
response.encoding = 'utf-8'

# r.url: 返回網址
# r.content: 返回網站內容
# r.status_code: 返回response的狀態碼
# r.headers: 返回response的標題訊息: DevTool->network->Response Headers
# print('1: ', response.text)
# print('2: ', response.encoding)
# print('3: ', response.url)
# print('4: ', response.content)
# print('5: ', response.status_code)
# print('6: ', response.headers)
# for k, v in response.headers.items():
#     print('6: ', k, ' -> ', v) 

# 1-1(補充) 下方為各種response的狀態碼
# 200 OK：一切正常。
# 301 Moved Permanently：永久搬家，會重新導向到新 url。
# 302 Found（Moved Temporarily）：暫時移到新位置。
# 400 Bad Request：明顯的用戶端錯誤，伺服器無法處理這個 Request。
# 401 Unauthorized：未授權，請求需攜帶憑證。
# 403 Forbidden：沒有權限。
# 404 Not Found：找不到資源。
# 418 I’m a teapot：我是一個茶壺，不會泡咖啡。(愚人節彩蛋)
# 500 Internal Server Error：伺服器端錯誤。
# 502 Bad Gateway：通常是伺服器的某個服務沒有正確執行。
# 503 Service Unavailable：伺服器臨時維護或是快掛了，暫時無法處理請求(臨時流量過大)。
# 504 Gateway Timeout：伺服器上的服務沒有回應。

# 需要UA
# url = https://www.rakuya.com.tw/
# 403
# url = 'https://ithelp.ithome.com.tw/' 