from  scrapy import cmdline
# 输出未过滤的页面信息
cmdline.execute('scrapy crawl tuicool'.split())
#cmdline.execute('scrapy crawl quotes1 -o quotes.json'.split())
# cmdline.execute('scrapy list'.split())

#测试网站http://www.qdcaijing.com/


#
# from scrapy.crawler import CrawlerProcess
# from spiders.quotes_spider import QuotesSpider
# from scrapy.utils.project import get_project_settings
# import schedule #调度
#
#
# def start_spider():
#
#   try:
#     # process = CrawlerProcess({
#     #       'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)'
#     # })
#     process = CrawlerProcess(settings=get_project_settings())
#     process.crawl(QuotesSpider)
#     process.start()
#     process.start()
#
#     print('-----------> 执行完成 <------------')
#   except Exception as e:
#     print('--出现错误--', e)
#     #email_spider('liepin', e) #发送邮件的方法，可以自己写
# def main():
#     print('开始检测，等待时间到达，开始执行')
#     schedule.every().day.at("22:00:55").do(start_spider)
#     while True:
#         schedule.run_pending()
# if __name__ == '__main__':
#     main()
#
#
