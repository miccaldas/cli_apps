import scrapy
#import snoop


class KEYBOARD_SPIDER(scrapy.Spider):
    name = 'keyboard_spider'

    start_urls = ['https://github.com/boppreh/keyboard']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'keyboard'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
