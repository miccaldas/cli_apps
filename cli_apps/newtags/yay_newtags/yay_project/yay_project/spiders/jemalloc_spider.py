import scrapy
#import snoop


class JEMALLOC_SPIDER(scrapy.Spider):
    name = 'jemalloc_spider'

    start_urls = ['http://www.canonware.com/jemalloc/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jemalloc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
