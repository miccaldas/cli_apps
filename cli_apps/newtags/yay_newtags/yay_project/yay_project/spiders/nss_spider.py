import scrapy
#import snoop


class NSS_SPIDER(scrapy.Spider):
    name = 'nss_spider'

    start_urls = ['https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nss'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
