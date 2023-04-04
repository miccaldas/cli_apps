import scrapy
#import snoop


class CAPSTONE_SPIDER(scrapy.Spider):
    name = 'capstone_spider'

    start_urls = ['https://www.capstone-engine.org/index.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'capstone'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
