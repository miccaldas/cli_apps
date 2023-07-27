import scrapy
#import snoop


class ISO8601_SPIDER(scrapy.Spider):
    name = 'iso8601_spider'

    start_urls = ['https://github.com/micktwomey/pyiso8601']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'iso8601'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
