import scrapy
#import snoop


class DEBUGEDIT_SPIDER(scrapy.Spider):
    name = 'debugedit_spider'

    start_urls = ['https://sourceware.org/debugedit/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'debugedit'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
