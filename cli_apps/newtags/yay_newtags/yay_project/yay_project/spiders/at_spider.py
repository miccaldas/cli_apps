import scrapy
#import snoop


class AT_SPIDER(scrapy.Spider):
    name = 'at_spider'

    start_urls = ['https://salsa.debian.org/debian/at']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'at'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
