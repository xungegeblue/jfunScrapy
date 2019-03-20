import scrapy


# 爬取数据到文件
class AuthorSpider(scrapy.Spider):
    name = "quotes1"
    # 保存配置https://www.jianshu.com/p/4de949ae713d
    # custom_settings = {
    #     'FEED_EXPORT_ENCODING': 'utf-8',
    #     'FEED_URI': 'xungege.jsonlines',
    # }

    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }