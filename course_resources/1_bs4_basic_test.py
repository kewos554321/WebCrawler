from bs4 import BeautifulSoup

html_doc = """
<html>
  <head>
    <title>Example</title>
  </head>
  <body>
    <h1 class='my-h1-class' id='my-h1-id'>Hello World</h1>
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

# 1: 請幫我使用bs4，解析上面的HTML語法，並且用Python變數接住解析後的HTML內容 (後面統一稱內容)

# 2-1. 請根據內容抓到第一個<span>的標籤 
# 2-2. 請根據內容抓到第一個<h1>標籤的所有內屬性及其中一個屬性的值

# 3-1 請使用find()方法抓到第一個id為'my-id'的<a>標籤
# 3-2 請使用find_all()方法抓到所有class為'my-class'的<a>標籤
# 3-3 請參考右側透過列表的方式抓所有的<li>及<span>標籤，參考:ex: soup.find_all(['li', 'a'])

# 4-1 請使用select()方法抓到所有的<li>標籤
# 4-2 請使用select()方法抓到所有id為my-id的標籤
# 4-3 請使用select()方法抓到所有class為yours-class的標籤
# 4-4 請使用select()方法抓到所有含有class內屬性的<a>標籤
# 4-5 請使用select()方法抓到第一個<ul>下所有的<a>標籤

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