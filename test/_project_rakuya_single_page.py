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
    
params = { # 台北市 南港區 公寓/華夏/套房 有車位 2房 
    'city': '0', 
    'zipcode': '115', 
    'sell_type': 'apartment%2CelevatorBuilding%2Cstudio',
    'parking': '1',
    'room': '2', 
    'sort': '11',
    'page': '1'
}

r = requests.get(url=url, params=params, headers=headers) # r: response

soup = BeautifulSoup(r.text, 'html.parser')
cards = soup.find_all('div', class_='list__item')
for i in range(len(cards)):
    card = cards[i]
    print(card)

    # months
    month = card.find('div', class_='item__month')
    item_months.append(month.get_text())

    # place
    place_area = card.find('span', class_='item__place-area')
    place_address = card.find('span', class_='item__place-address')
    card_data_url = card.attrs.get('data-url')
    place_community = card.find('span', class_='item__place-community')
    place_community_data_url = place_community.attrs.get('data-url')
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
    ping = ping_number.get_text() + "_" + ping_unit.get_text()
    item_pings.append(ping)

    # price-total
    price_total_info = card.find('div', class_='item__price-total')
    price_total_number = price_total_info.find('span', class_='item__number')
    price_total_unit = price_total_info.find('span', class_='item__unit')
    price_total = price_total_number.get_text() + "_" + price_total_unit.get_text()
    item_price_totals.append(price_total)

    # price-unit
    price_unit_info = card.find('div', class_='item__price-unit')
    price_unit_number = price_unit_info.find('span', class_='item__number')
    price_unit_unit = price_unit_info.find('span', class_='item__unit')
    price_unit = price_unit_number.get_text() + "_" + price_unit_unit.get_text()
    item_price_units.append(price_unit)

    print(item_months)
    print(item_places)
    print(item_mixes)
    print(item_pings)
    print(item_price_totals)
    print(item_price_units)
    exit()