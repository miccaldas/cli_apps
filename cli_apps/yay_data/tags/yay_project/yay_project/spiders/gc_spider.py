import scrapy
#import snoop


class GC_SPIDER(scrapy.Spider):
    name = 'gc_spider'

    start_urls = ['https://www.hboehm.info/gc/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
