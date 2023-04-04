import scrapy
#import snoop


class PANGO_SPIDER(scrapy.Spider):
    name = 'pango_spider'

    start_urls = ['https://www.pango.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pango'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
