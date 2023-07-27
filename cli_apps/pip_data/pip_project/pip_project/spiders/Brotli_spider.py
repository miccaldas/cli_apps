import scrapy
#import snoop


class BROTLI_SPIDER(scrapy.Spider):
    name = 'Brotli_spider'

    start_urls = ['https://github.com/google/brotli']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'Brotli'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
