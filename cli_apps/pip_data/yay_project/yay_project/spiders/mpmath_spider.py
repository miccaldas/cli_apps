import scrapy
#import snoop


class MPMATH_SPIDER(scrapy.Spider):
    name = 'mpmath_spider'

    start_urls = ['http://mpmath.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mpmath'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
