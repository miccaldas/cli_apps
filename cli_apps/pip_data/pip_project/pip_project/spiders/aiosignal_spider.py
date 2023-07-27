import scrapy
#import snoop


class AIOSIGNAL_SPIDER(scrapy.Spider):
    name = 'aiosignal_spider'

    start_urls = ['https://github.com/aio-libs/aiosignal']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'aiosignal'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
