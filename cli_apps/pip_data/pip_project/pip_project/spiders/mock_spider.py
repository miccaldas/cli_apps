import scrapy
#import snoop


class MOCK_SPIDER(scrapy.Spider):
    name = 'mock_spider'

    start_urls = ['http://mock.readthedocs.org/en/latest/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mock'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
