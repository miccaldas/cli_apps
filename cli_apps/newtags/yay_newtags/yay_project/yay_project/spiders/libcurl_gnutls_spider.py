import scrapy
#import snoop


class LIBCURL_GNUTLS_SPIDER(scrapy.Spider):
    name = 'libcurl_gnutls_spider'

    start_urls = ['https://curl.haxx.se/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcurl-gnutls'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
