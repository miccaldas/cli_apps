import scrapy
#import snoop


class GRAPHENE_SPIDER(scrapy.Spider):
    name = 'graphene_spider'

    start_urls = ['https://ebassi.github.io/graphene/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'graphene'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
