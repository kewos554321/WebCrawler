import requests

# url = 'https://k-3325-bbg.thisiscdn.com/bcdn_token=GtUWpLKeasV_SQmllI34ggYP709B9txjgHdWfg-IYYU&expires=1674829921&token_path=%2Fe68a59ce-9ad0-4f13-ab99-f917ddd52901%2F/e68a59ce-9ad0-4f13-ab99-f917ddd52901/640x360/video.m3u8'

# headers = {
#     'authority': 'k-3325-bbg.thisiscdn.com',
#     'method': 'GET',
#     'path': '/bcdn_token=GtUWpLKeasV_SQmllI34ggYP709B9txjgHdWfg-IYYU&expires=1674829921&token_path=%2Fe68a59ce-9ad0-4f13-ab99-f917ddd52901%2F/e68a59ce-9ad0-4f13-ab99-f917ddd52901/playlist.m3u8',
#     'scheme': 'https',
#     'accept': '*/*',
#     'accept-encoding': 'gzip, deflate, br',
#     'accept-language': 'zh-TW,zh;q=0.9',
#     'origin': 'https://missav.com',
#     'referer': 'https://missav.com/stars-333',
#     'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"macOS"',
#     'sec-fetch-dest': 'empty',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'cross-site',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
# }

# response = requests.get(url=url, headers=headers)
# print(response)
# print(response.text)

url = 'https://k-3325-bbg.thisiscdn.com/bcdn_token=GtUWpLKeasV_SQmllI34ggYP709B9txjgHdWfg-IYYU&expires=1674829921&token_path=%2Fe68a59ce-9ad0-4f13-ab99-f917ddd52901%2F/e68a59ce-9ad0-4f13-ab99-f917ddd52901/640x360/video33.ts'

headers = {
    'authority': 'k-3325-bbg.thisiscdn.com',
    'method': 'GET',
    'path': '/bcdn_token=GtUWpLKeasV_SQmllI34ggYP709B9txjgHdWfg-IYYU&expires=1674829921&token_path=%2Fe68a59ce-9ad0-4f13-ab99-f917ddd52901%2F/e68a59ce-9ad0-4f13-ab99-f917ddd52901/640x360/video33.ts',
    'scheme': 'https',
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-TW,zh;q=0.9',
    'origin': 'https://missav.com',
    'referer': 'https://missav.com/stars-333',
    'sec-ch-ua': '"Not?A_Brand";v="8", "Chromium";v="108", "Google Chrome";v="108"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}
response = requests.get(url=url, headers=headers, stream=True)
print(response)
response.encoding='utf-8'
print(response.content)
with open('./video33.mp4', 'wb') as file:
    for chunk in response.iter_content(chunk_size = 1024*1024):
        if chunk:
            file.write(response.content)