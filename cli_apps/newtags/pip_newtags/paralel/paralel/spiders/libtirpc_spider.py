import scrapy
#import snoop


class LIBTIRPC_SPIDER(scrapy.Spider):
    name = 'libtirpc_spider'

    start_urls = ['https://github.com/alisw/libtirpc']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libtirpc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
