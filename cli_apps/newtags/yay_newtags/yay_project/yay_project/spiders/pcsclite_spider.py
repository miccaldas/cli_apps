import scrapy
#import snoop


class PCSCLITE_SPIDER(scrapy.Spider):
    name = 'pcsclite_spider'

    start_urls = ['https://pcsclite.apdu.fr/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pcsclite'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results