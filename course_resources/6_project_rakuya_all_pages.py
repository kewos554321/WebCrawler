import requests
from bs4 import BeautifulSoup

url = 'https://www.rakuya.com.tw/realprice/result?' #樂屋網實價登入

headers = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
}

item_months = []
item_places = []
item_mixes = []
item_pings = []
item_price_totals = []
item_price_units = []

page_index = 0

while True:

    # 每輪index加1
    page_index+=1
    params = { # 台北市 南港區 公寓/華夏/套房 有車位 2房 
        'city': '0', 
        'zipcode': '115', 
        'sell_type': 'apartment%2CelevatorBuilding%2Cstudio',
        'parking': '1',
        'room': '2', 
        'sort': '11',
        'page': page_index
    }

    r = requests.get(url=url, params=params, headers=headers) # r: response

    # 檢查狀態碼
    if r.status_code != 200: 
        print('status error')
        break

    soup = BeautifulSoup(r.text, 'html.parser')

    # 檢查是否超過最後一頁
    block_info = soup.select('div.block__remark > p')
    if (len(block_info) != 0):
        print('has over the lastest page')
        break

    # bs4分析頁面
    soup = BeautifulSoup(r.text, 'html.parser')
    cards = soup.find_all('div', class_='list__item')
    for i in range(len(cards)):
        card = cards[i]
        # print(card)

        # months
        month = card.find('div', class_='item__month')
        item_months.append(month.get_text())

        # place
        place_area = card.find('span', class_='item__place-area')
        place_address = card.find('span', class_='item__place-address')
        card_data_url = card.attrs.get('data-url')
        place_community = card.find('span', class_='item__place-community')
        try:
            place_community_data_url = place_community.attrs.get('data-url')
        except AttributeError:
            place_community = BeautifulSoup('<div>None</div>', 'html.parser')
            place_community_data_url = 'None'
        place = place_area.get_text() + "_" + place_address.get_text() + "_" + card_data_url + "_" +\
            place_community.get_text() + "_" + place_community_data_url
        item_places.append(place)

        # mix
        mix_infos = card.select('div.item__mix > span')
        mix_info_summary = mix_infos[0].get_text()
        for j in range(1, len(mix_infos)):
            mix_info_summary = mix_info_summary + "_"
            mix_info = mix_infos[j].get_text()
            mix_info_summary = mix_info_summary + mix_info
        item_mixes.append(mix_info_summary)

        # ping
        ping_info = card.find('div', class_='item__ping')
        ping_number = ping_info.find('span', class_='item__number')
        ping_unit = ping_info.find('span', class_='item__unit')
        ping_remark = ping_info.find('span', class_='item__remark')
        if ping_remark is None:
            ping_remark = BeautifulSoup('<div>None</div>', 'html.parser')
        ping = ping_number.get_text() + "_" + ping_unit.get_text() + \
            "_" + ping_remark.get_text()
        item_pings.append(ping)

        # price-total
        price_total_info = card.find('div', class_='item__price-total')
        price_total_number = price_total_info.find('span', class_='item__number')
        price_total_unit = price_total_info.find('span', class_='item__unit')
        price_total_remark = price_total_info.find('span', class_='item__remark')
        if price_total_remark is None:
            price_total_remark = BeautifulSoup('<div>None</div>', 'html.parser')
        price_total = price_total_number.get_text() + "_" + price_total_unit.get_text() + \
            "_" + price_total_remark.get_text()
        
        item_price_totals.append(price_total)

        # price-unit
        price_unit_info = card.find('div', class_='item__price-unit')
        price_unit_number = price_unit_info.find('span', class_='item__number')
        price_unit_unit = price_unit_info.find('span', class_='item__unit')
        price_unit_remark = price_unit_info.find('span', class_='item__remark')
        if price_unit_remark is None:
            price_unit_remark = BeautifulSoup('<div>None</div>', 'html.parser')
        price_unit = price_unit_number.get_text() + "_" + price_unit_unit.get_text() + \
            "_" + price_unit_remark.get_text()


        item_price_units.append(price_unit)

# print(item_months)
# print(item_places)
# print(item_mixes)
# print(item_pings)
# print(item_price_totals)
# print(item_price_units)

# print(len(item_months))
# print(len(item_places))

# save to file

import pandas as pd

# Create a dataframe
data = {
    '交易日期': item_months, 
    '區_地址_詳細說明連結_建案名稱_此建案詳細說明連結': item_places, 
    '房型_大樓類型_售出類型_所在樓層': item_mixes, 
    '總坪數_總坪數單位_總坪數備註': item_pings, 
    '總價格_總價格單位_總價格備註': item_price_totals, 
    '每坪價格_每坪價格單位_每坪價格備註': item_price_units,  
    }
df = pd.DataFrame(data)

# Save the dataframe as an Excel file
df.to_excel('./output.xlsx', index=False)


