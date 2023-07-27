import scrapy
#import snoop


class FQDN_SPIDER(scrapy.Spider):
    name = 'fqdn_spider'

    start_urls = ['https://github.com/ypcrts/fqdn']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fqdn'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
