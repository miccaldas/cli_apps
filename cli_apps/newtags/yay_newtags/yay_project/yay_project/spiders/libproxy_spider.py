import scrapy
#import snoop


class LIBPROXY_SPIDER(scrapy.Spider):
    name = 'libproxy_spider'

    start_urls = ['https://libproxy.github.io/libproxy/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libproxy'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
