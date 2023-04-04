import scrapy
#import snoop


class LIBKEYBINDER3_SPIDER(scrapy.Spider):
    name = 'libkeybinder3_spider'

    start_urls = ['https://github.com/engla/keybinder/tree/keybinder-3.0']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libkeybinder3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
