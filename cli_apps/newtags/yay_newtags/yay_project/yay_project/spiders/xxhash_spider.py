import scrapy
#import snoop


class XXHASH_SPIDER(scrapy.Spider):
    name = 'xxhash_spider'

    start_urls = ['https://cyan4973.github.io/xxHash/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xxhash'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
