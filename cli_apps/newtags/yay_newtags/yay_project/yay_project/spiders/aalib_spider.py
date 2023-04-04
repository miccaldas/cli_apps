import scrapy
#import snoop


class AALIB_SPIDER(scrapy.Spider):
    name = 'aalib_spider'

    start_urls = ['http://aa-project.sourceforge.net/aalib/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'aalib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
