import scrapy
#import snoop


class SPICE_PROTOCOL_SPIDER(scrapy.Spider):
    name = 'spice_protocol_spider'

    start_urls = ['https://spice-space.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'spice-protocol'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
