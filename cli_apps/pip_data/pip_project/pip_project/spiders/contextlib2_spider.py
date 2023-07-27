import scrapy
#import snoop


class CONTEXTLIB2_SPIDER(scrapy.Spider):
    name = 'contextlib2_spider'

    start_urls = ['http://contextlib2.readthedocs.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'contextlib2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
