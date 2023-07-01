import scrapy
import random
from scrapy.http import HtmlResponse

class RakuyaSpider(scrapy.Spider):
    name = 'rakuya'
    allowed_domains = ['www.rakuya.com.tw']
    start_urls = ['http://www.rakuya.com.tw/']

    # handle_httpstatus_list = [301]

    user_agent_list = [
        "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
    ]

    def start_requests(self):
        headers = {
            'User-Agent': random.choice(self.user_agent_list)
        }
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=headers)

    def parse(self, response:HtmlResponse):
        if not isinstance(response.status, int): 
            print('errorrrrrrrrrrrrrrrrrrrrrrrrrrrrr')
            return
        print('1: ', response.url) # 回應的URL;當前網頁的URL
        print('2: ', response.status) # HTTP狀態碼
        print('3: ', response.headers) 
        print('4: ', response.body) # 以二進制形式給網頁文字 開頭有b'
        print('5: ', response.text) # 給網頁文字
        print('6: ', response.request)
        print('7: ', response.meta)
        print('8: ', response.urljoin('/123456')) #修改原來url
        print('9: ', response.xpath('//*[@id="root"]/div/div[3]/div[2]/div/main/div/div[3]/div/div/div[1]/article[1]/div/div/div/div/div/div[2]/div/div[1]/div/div/div/div[1]/div[1]/div[1]/a/div[1]/h2'))
        print('10: ', response.css('h1'))
        print('11: ', response.selector)
        print('12: ', response.encoding)
        print('13: ', response.headers)
        print('14: ', response.flags)
        pass
    
    def errback(self, failure, response):
        self.logger.error(repr(failure))
        print('1111111111111error: ', self.logger.error(repr(failure)))
        yield scrapy.Request(url=response.url, callback=self.parse, errback=self.errback)