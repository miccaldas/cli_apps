import scrapy
#import snoop


class GUMBO_PARSER_SPIDER(scrapy.Spider):
    name = 'gumbo_parser_spider'

    start_urls = ['https://github.com/google/gumbo-parser']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gumbo-parser'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
