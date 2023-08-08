import scrapy
#import snoop


class MPFR_SPIDER(scrapy.Spider):
    name = 'mpfr_spider'

    start_urls = ['https://www.mpfr.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mpfr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
