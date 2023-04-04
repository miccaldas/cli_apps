import scrapy
#import snoop


class LIBDV_SPIDER(scrapy.Spider):
    name = 'libdv_spider'

    start_urls = ['http://libdv.sourceforge.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libdv'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
