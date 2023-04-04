import scrapy
#import snoop


class ATOOL_SPIDER(scrapy.Spider):
    name = 'atool_spider'

    start_urls = ['https://www.nongnu.org/atool']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'atool'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
