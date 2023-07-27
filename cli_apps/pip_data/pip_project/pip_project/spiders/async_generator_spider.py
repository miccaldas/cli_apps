import scrapy
#import snoop


class ASYNC_GENERATOR_SPIDER(scrapy.Spider):
    name = 'async_generator_spider'

    start_urls = ['https://github.com/python-trio/async_generator']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'async-generator'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
