import scrapy
#import snoop


class BRIDGE_UTILS_SPIDER(scrapy.Spider):
    name = 'bridge_utils_spider'

    start_urls = ['https://wiki.linuxfoundation.org/networking/bridge']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'bridge-utils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
