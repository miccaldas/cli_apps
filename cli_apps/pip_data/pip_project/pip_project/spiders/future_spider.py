import scrapy
#import snoop


class FUTURE_SPIDER(scrapy.Spider):
    name = 'future_spider'

    start_urls = ['https://python-future.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'future'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
