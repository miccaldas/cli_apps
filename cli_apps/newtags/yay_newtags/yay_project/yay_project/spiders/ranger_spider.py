import scrapy
#import snoop


class RANGER_SPIDER(scrapy.Spider):
    name = 'ranger_spider'

    start_urls = ['https://ranger.github.io']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ranger'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
