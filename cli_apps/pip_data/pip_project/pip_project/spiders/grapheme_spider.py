import scrapy
#import snoop


class GRAPHEME_SPIDER(scrapy.Spider):
    name = 'grapheme_spider'

    start_urls = ['https://github.com/alvinlindstam/grapheme']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'grapheme'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
