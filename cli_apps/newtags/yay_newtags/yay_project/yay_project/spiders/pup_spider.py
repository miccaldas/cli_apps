import scrapy
#import snoop


class PUP_SPIDER(scrapy.Spider):
    name = 'pup_spider'

    start_urls = ['https://github.com/ericchiang/pup']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pup'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
