import scrapy
#import snoop


class DEBUGPY_SPIDER(scrapy.Spider):
    name = 'debugpy_spider'

    start_urls = ['https://aka.ms/debugpy']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'debugpy'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
