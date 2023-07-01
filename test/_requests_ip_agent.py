import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.us-proxy.org/'
headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')
pre_id_list = soup.find('textarea', class_='form-control').get_text().split('\n')
id_list = []
for id in pre_id_list:
    try:
        check_fst = int(id[0])
        id_list.append(id)
    except ValueError:
        continue
    except IndexError:
        continue
print(id_list)


url = 'https://httpbin.org/ip'

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}


order = 0
for id in id_list:
    order+=1
    proxies = {
        'http': id
    }
    response = requests.get(url=url, headers=headers, proxies=proxies)
    content = json.loads(response.text)
    origin = content['origin']
    if origin == id:
        print(f'{order}, res:{origin}, pro:{id}')

# with open('./requests-ip-agent-example.html', 'w', encoding='utf-8') as file:
#     file.write(content)

