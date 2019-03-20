from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
import random
import random
from scrapy import signals


class MyUserAgentMiddleware(UserAgentMiddleware):

    def __init__(self, user_agent):
        self.user_agent = user_agent

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            user_agent=crawler.settings.get('CUSTOM_USER_AGENT')
        )

    def process_request(self, request, spider):
        agent = random.choice(self.user_agent)
        print(agent)
        request.headers['User-Agent'] = agent