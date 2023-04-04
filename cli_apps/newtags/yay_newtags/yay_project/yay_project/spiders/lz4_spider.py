import scrapy
#import snoop


class LZ4_SPIDER(scrapy.Spider):
    name = 'lz4_spider'

    start_urls = ['https://lz4.github.io/lz4/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'lz4'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
