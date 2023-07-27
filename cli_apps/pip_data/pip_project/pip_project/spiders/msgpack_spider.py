import scrapy
#import snoop


class MSGPACK_SPIDER(scrapy.Spider):
    name = 'msgpack_spider'

    start_urls = ['https://msgpack.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'msgpack'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
