import scrapy
#import snoop


class LIBMPC_SPIDER(scrapy.Spider):
    name = 'libmpc_spider'

    start_urls = ['http://www.multiprecision.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libmpc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
