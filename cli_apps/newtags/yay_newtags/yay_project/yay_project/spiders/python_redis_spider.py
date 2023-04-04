import scrapy
#import snoop


class PYTHON_REDIS_SPIDER(scrapy.Spider):
    name = 'python_redis_spider'

    start_urls = ['https://github.com/redis/redis-py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-redis'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
