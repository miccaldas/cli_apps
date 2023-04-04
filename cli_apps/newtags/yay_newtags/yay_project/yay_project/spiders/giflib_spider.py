import scrapy
#import snoop


class GIFLIB_SPIDER(scrapy.Spider):
    name = 'giflib_spider'

    start_urls = ['http://giflib.sourceforge.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'giflib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
