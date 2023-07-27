import scrapy
#import snoop


class APPDIRS_SPIDER(scrapy.Spider):
    name = 'appdirs_spider'

    start_urls = ['http://github.com/ActiveState/appdirs']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'appdirs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
