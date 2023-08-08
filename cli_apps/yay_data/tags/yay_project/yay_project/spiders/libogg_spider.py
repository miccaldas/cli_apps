import scrapy
#import snoop


class LIBOGG_SPIDER(scrapy.Spider):
    name = 'libogg_spider'

    start_urls = ['https://www.xiph.org/ogg/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libogg'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
