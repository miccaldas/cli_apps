import scrapy
#import snoop


class OBJGRAPH_SPIDER(scrapy.Spider):
    name = 'objgraph_spider'

    start_urls = ['https://mg.pov.lt/objgraph/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'objgraph'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
