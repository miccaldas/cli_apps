import scrapy
#import snoop


class DMENU_SPIDER(scrapy.Spider):
    name = 'dmenu_spider'

    start_urls = ['https://tools.suckless.org/dmenu/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dmenu'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
