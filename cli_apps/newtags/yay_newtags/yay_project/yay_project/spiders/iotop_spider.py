import scrapy
#import snoop


class IOTOP_SPIDER(scrapy.Spider):
    name = 'iotop_spider'

    start_urls = ['http://guichaz.free.fr/iotop/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'iotop'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
