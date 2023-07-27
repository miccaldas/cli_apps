import scrapy
#import snoop


class NBCLASSIC_SPIDER(scrapy.Spider):
    name = 'nbclassic_spider'

    start_urls = ['https://github.com/jupyter/nbclassic']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nbclassic'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
