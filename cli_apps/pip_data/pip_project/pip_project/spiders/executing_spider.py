import scrapy
#import snoop


class EXECUTING_SPIDER(scrapy.Spider):
    name = 'executing_spider'

    start_urls = ['https://github.com/alexmojaki/executing']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'executing'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
