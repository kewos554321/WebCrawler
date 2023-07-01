from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p class='my-class'>This is an example webpage.</p>
    <ul>
        <li>RED</li>
        <li class='my-li-class'>BLUE</li>
        <li id='my-li-id'>GREEN</li>
        <li id='my-li-id'>ORANGE</li>
        <li class='my-li-class'>YELLOW</li>
        <a href='https://www.google.com.tw/' id='my-id'>LinkToGoogle</a>
        <a href='https://medium.com/' class='my-class'>LinkToMedium</a>
    </ul>
    <a href='https://www.youtube.com/' class='yours-class'>LinkToYoutube</a>
    <div>
        <span>This is a span.</span>
        <p>This is a statement.</p>
        <p>This is an another statement.</p>
        <h1>This is a header</h1>
        <ul>
            <p>This is a the other statement.</p>
        </ul>
    </div>
  </body>
</html>
"""


# 1-1 
# 解析HTML語法，語法可能來自requests下載後及本地端輸入
# 在此以寫死HTML示範
soup = BeautifulSoup(html_doc, 'html.parser')
# print('1: ', soup)

# 2-1 
# 根據標籤名字找節點 
# 找到的是第一個符合的tag
# print('1: ', soup.a)

# 2-2 
# 獲取標籤屬性及其值
# print('1:', soup.a.attrs)
# print('2:', soup.a.attrs['href'])

# 3-1 bs4函數: find()
# 返回第一個符合的tag
# print('1: ', soup.find('ul'))
# print('2: ', soup.find('ul', class_='my-li-class'))
# print('3: ', soup.find('ul', id='my-li-id'))
# print('4: ', soup.find('li'))
# print('5: ', soup.find('li', class_='my-li-class'))
# print('6: ', soup.find('li', id='my-li-id'))

# 3-2 bs4函數: find_all()
# 返回所有對應標籤的列表
# print('1: ', soup.find_all('li'))
# print('2: ', soup.find_all('li', id='my-li-id'))

# 若要返回多組對應標籤資料，參數要用列表
# print('1: ', soup.find_all(['li', 'a']))

# 可以用limit查找前幾筆
# print('1: ', soup.find_all('li', limit=2))

# 3-3 bs4函數: select()：根據css選擇器來獲得對象 
# 會返回所有對應標籤的列表
# print('1: ', soup.select('a'))

# 透過.來表達class選擇器及透過＃來表達id選擇器
# print('1: ', soup.select('.my-li-class'))
# print('2: ', soup.select('#my-li-id'))

# 透過屬性查找
# print('1: ', soup.select('a[class]'))
# print('2: ', soup.select('li[class="my-li-class"]'))

# 透過層級選擇器查找
# 'div p'：表示找div下層所有p
# 'div > p': 表示找div下層的p
# 'div > p, span': 表示找div下的p跟span
# print('1: ', soup.select('div p'))
# print('2: ', soup.select('div > p'))
# print('3: ', soup.select('div > ul > p'))
# print('4: ', soup.select('div > p, span'))

# 4-1 擷取標籤內文字
# 有兩個方法:1. `.string` 2. `get_text()`
# obj = soup.select('div p')
# for i in range(len(obj)):
#     print(f'{i}:', obj[i])
#     print(f'{i}:', obj[i].string)
#     print(f'{i}:', obj[i].get_text())

# 獲取屬性值: 有下面三種方式
# obj = soup.select('a')
# print(obj[0])
# print(obj[0].attrs.get('href'))
# print(obj[0].get('href'))
# print(obj[0]['href'])