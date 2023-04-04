import scrapy
#import snoop


class CAIRO_SPIDER(scrapy.Spider):
    name = 'cairo_spider'

    start_urls = ['https://cairographics.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cairo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
