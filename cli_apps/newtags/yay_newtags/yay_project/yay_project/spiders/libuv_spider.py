import scrapy
#import snoop


class LIBUV_SPIDER(scrapy.Spider):
    name = 'libuv_spider'

    start_urls = ['https://github.com/libuv/libuv']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libuv'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
