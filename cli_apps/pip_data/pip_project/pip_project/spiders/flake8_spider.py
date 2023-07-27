import scrapy
#import snoop


class FLAKE8_SPIDER(scrapy.Spider):
    name = 'flake8_spider'

    start_urls = ['https://github.com/pycqa/flake8']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'flake8'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
