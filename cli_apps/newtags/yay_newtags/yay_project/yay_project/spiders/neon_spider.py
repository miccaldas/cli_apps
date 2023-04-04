import scrapy
#import snoop


class NEON_SPIDER(scrapy.Spider):
    name = 'neon_spider'

    start_urls = ['https://notroj.github.io/neon/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'neon'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
