import scrapy
#import snoop


class COLR_SPIDER(scrapy.Spider):
    name = 'colr_spider'

    start_urls = ['https://learn.microsoft.com/en-us/typography/opentype/spec/colr']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'colr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
