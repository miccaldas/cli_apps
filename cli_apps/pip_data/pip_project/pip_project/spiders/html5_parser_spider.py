import scrapy
#import snoop


class HTML5_PARSER_SPIDER(scrapy.Spider):
    name = 'html5_parser_spider'

    start_urls = ['https://html5-parser.readthedocs.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'html5-parser'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
