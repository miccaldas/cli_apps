import scrapy
#import snoop


class WMCTRL_SPIDER(scrapy.Spider):
    name = 'wmctrl_spider'

    start_urls = ['http://tripie.sweb.cz/utils/wmctrl/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'wmctrl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
