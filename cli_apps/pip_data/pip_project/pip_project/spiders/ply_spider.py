import scrapy
#import snoop


class PLY_SPIDER(scrapy.Spider):
    name = 'ply_spider'

    start_urls = ['http://www.dabeaz.com/ply/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ply'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
