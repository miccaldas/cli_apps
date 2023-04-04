import scrapy
#import snoop


class ZSTD_SPIDER(scrapy.Spider):
    name = 'zstd_spider'

    start_urls = ['https://facebook.github.io/zstd/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'zstd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
