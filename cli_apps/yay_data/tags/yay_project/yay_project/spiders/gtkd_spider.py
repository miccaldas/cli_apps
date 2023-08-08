import scrapy
#import snoop


class GTKD_SPIDER(scrapy.Spider):
    name = 'gtkd_spider'

    start_urls = ['https://gtkd.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gtkd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
