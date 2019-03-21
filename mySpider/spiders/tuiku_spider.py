import scrapy
from scrapy.utils.project import get_project_settings
from scrapy.utils.response import open_in_browser
from scrapy.selector import Selector
#xpath参考地址https://blog.csdn.net/Co_zy/article/details/78333540?locationNum=8&fps=1
class QuotesSpider(scrapy.Spider):
    name = "tuicool"

    def start_requests(self):
        urls = [
            'https://www.tuicool.com/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        articleItem = response.xpath('//*[@id="list_article"]/div').getall()

        for it in articleItem:
            img = Selector(text=it).xpath('//div/img/@src').get()
            title = Selector(text=it).xpath('//div/a/@title').get()
            org = Selector(text=it).xpath('//div[@class="tip"]/span[1]/text()').get()
            time = Selector(text=it).xpath('//div[@class="tip"]/span[3]/text()').get()
            print ("%s %s %s" %(img,title,time))

        # from scrapy.shell import inspect_response
        # inspect_response(response, self)

        # open_in_browser(response) #直接在浏览器打开爬取到的网页
        # 保存爬取到的网页
        # with open("tuicool.html", 'wb') as f:
        #     f.write(response.body)