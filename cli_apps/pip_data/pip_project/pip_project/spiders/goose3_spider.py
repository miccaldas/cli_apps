import scrapy
#import snoop


class GOOSE3_SPIDER(scrapy.Spider):
    name = 'goose3_spider'

    start_urls = ['https://github.com/goose3/goose3']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'goose3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
