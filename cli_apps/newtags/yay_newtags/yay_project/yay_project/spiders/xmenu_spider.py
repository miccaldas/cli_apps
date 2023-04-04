import scrapy
#import snoop


class XMENU_SPIDER(scrapy.Spider):
    name = 'xmenu_spider'

    start_urls = ['https://github.com/phillbush/xmenu']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xmenu'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
