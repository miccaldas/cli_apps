import scrapy
#import snoop


class LIBPNG_SPIDER(scrapy.Spider):
    name = 'libpng_spider'

    start_urls = ['http://www.libpng.org/pub/png/libpng.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libpng'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
