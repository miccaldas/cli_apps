import scrapy
#import snoop


class POE_API_SPIDER(scrapy.Spider):
    name = 'poe_api_spider'

    start_urls = ['https://github.com/ading2210/poe-api']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'poe-api'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
