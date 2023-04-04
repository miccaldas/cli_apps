import scrapy
#import snoop


class NSPR_SPIDER(scrapy.Spider):
    name = 'nspr_spider'

    start_urls = ['https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSPR']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nspr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
