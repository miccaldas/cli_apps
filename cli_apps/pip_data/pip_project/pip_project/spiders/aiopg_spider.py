import scrapy
#import snoop


class AIOPG_SPIDER(scrapy.Spider):
    name = 'aiopg_spider'

    start_urls = ['https://aiopg.readthedocs.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'aiopg'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
