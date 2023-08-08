import scrapy
#import snoop


class ISO_CODES_SPIDER(scrapy.Spider):
    name = 'iso_codes_spider'

    start_urls = ['https://salsa.debian.org/iso-codes-team/iso-codes']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'iso-codes'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
