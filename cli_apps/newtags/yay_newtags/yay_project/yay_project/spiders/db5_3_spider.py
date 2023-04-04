import scrapy
#import snoop


class DB5_3_SPIDER(scrapy.Spider):
    name = 'db5_3_spider'

    start_urls = ['https://www.oracle.com/technology/software/products/berkeley-db/index.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'db5.3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
