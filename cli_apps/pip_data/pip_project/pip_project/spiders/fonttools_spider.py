import scrapy
#import snoop


class FONTTOOLS_SPIDER(scrapy.Spider):
    name = 'fonttools_spider'

    start_urls = ['http://github.com/fonttools/fonttools']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fonttools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
