import scrapy
#import snoop


class MINIUPNPC_SPIDER(scrapy.Spider):
    name = 'miniupnpc_spider'

    start_urls = ['https://miniupnp.tuxfamily.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'miniupnpc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
