import scrapy
#import snoop


class WOLFSSL_SPIDER(scrapy.Spider):
    name = 'wolfssl_spider'

    start_urls = ['https://www.wolfssl.com/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'wolfssl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
