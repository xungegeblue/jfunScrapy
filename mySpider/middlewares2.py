import fake_useragent

class RandomUserAgentMiddleware(object):

    def __init__(self):
        self.agent = fake_useragent.UserAgent(use_cache_server=False)

    @classmethod
    def from_crawler(cls, crawler):
        return cls()

    def process_request(self, request, spider):

        request.headers['User-Agent'] = self.agent.chrome;

        # print(ua.ie)  # 随机打印ie浏览器任意版本
        # print(ua.firefox)  # 随机打印firefox浏览器任意版本
        # print(ua.chrome)  # 随机打印chrome浏览器任意版本
        # print(ua.random)  # 随机打印任意厂家的浏览器
