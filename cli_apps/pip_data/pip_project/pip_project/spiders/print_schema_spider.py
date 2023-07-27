import scrapy
#import snoop


class PRINT_SCHEMA_SPIDER(scrapy.Spider):
    name = 'print_schema_spider'

    start_urls = ['https://github.com/suryashekharc/print_schema']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'print-schema'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
