import scrapy


class MediumSpider(scrapy.Spider):
    name = 'medium' # 爬蟲的名字 在運行爬蟲時 使用的值
    allowed_domains = ['medium.com'] # 允許訪問的域名
    start_urls = ['http://medium.com/'] # 起始的url域名  第一次訪問的域名

    def parse(self, response): # 相當request.get後返回的response
        # print('1: ', response.url) # 回應的URL;當前網頁的URL
        # print('2: ', response.status) # HTTP狀態碼
        # print('3: ', response.headers) 
        # print('4: ', response.body) # 以二進制形式給網頁文字 開頭有b'
        # print('5: ', response.text) # 給網頁文字
        # print('6: ', response.request)
        # print('7: ', response.meta)
        # print('8: ', response.urljoin('/123456')) #修改原來url
        # print('9: ', response.xpath('//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[3]/div/div/div[1]/article[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2'))
        # print('10: ', response.css('h1'))
        # print('11: ', response.selector)
        # print('12: ', response.encoding)
        # print('13: ', response.headers)
        # print('14: ', response.flags)
        pass
