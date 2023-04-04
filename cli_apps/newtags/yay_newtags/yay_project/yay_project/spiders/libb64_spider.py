import scrapy
#import snoop


class LIBB64_SPIDER(scrapy.Spider):
    name = 'libb64_spider'

    start_urls = ['http://libb64.sourceforge.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libb64'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
