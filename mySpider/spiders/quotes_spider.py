import scrapy
from scrapy.utils.project import get_project_settings


class QuotesSpider(scrapy.Spider):
    name = "xgg"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        settings = get_project_settings()
        LOG_LEVEL = settings.get("LOG_LEVEL")
        print ('LOG_LEVEL:'+LOG_LEVEL)
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        print('User-Agent:')
        print(response.request.headers['User-Agent'])
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)