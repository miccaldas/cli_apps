import scrapy
#import snoop


class ELIXIR_SPIDER(scrapy.Spider):
    name = 'Elixir_spider'

    start_urls = ['http://elixir.ematia.de']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'Elixir'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
