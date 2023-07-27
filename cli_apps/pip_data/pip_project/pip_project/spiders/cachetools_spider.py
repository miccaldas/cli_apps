import scrapy
#import snoop


class CACHETOOLS_SPIDER(scrapy.Spider):
    name = 'cachetools_spider'

    start_urls = ['https://github.com/tkem/cachetools/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cachetools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
