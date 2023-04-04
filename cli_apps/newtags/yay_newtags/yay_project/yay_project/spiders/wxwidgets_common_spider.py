import scrapy
#import snoop


class WXWIDGETS_COMMON_SPIDER(scrapy.Spider):
    name = 'wxwidgets_common_spider'

    start_urls = ['https://wxwidgets.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'wxwidgets-common'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
