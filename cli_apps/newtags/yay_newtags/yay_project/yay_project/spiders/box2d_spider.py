import scrapy
#import snoop


class BOX2D_SPIDER(scrapy.Spider):
    name = 'box2d_spider'

    start_urls = ['http://www.box2d.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'box2d'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
