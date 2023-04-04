import scrapy
#import snoop


class MTDEV_SPIDER(scrapy.Spider):
    name = 'mtdev_spider'

    start_urls = ['https://bitmath.org/code/mtdev/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mtdev'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
