import scrapy
#import snoop


class DEVICE_MAPPER_SPIDER(scrapy.Spider):
    name = 'device_mapper_spider'

    start_urls = ['http://sourceware.org/dm/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'device-mapper'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
