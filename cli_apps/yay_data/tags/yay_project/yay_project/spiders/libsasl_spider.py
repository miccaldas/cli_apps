import scrapy
#import snoop


class LIBSASL_SPIDER(scrapy.Spider):
    name = 'libsasl_spider'

    start_urls = ['https://www.cyrusimap.org/sasl/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsasl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
