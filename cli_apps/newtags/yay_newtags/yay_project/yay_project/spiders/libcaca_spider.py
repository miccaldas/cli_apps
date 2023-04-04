import scrapy
#import snoop


class LIBCACA_SPIDER(scrapy.Spider):
    name = 'libcaca_spider'

    start_urls = ['http://caca.zoy.org/wiki/libcaca']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcaca'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
