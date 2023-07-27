import scrapy
#import snoop


class LXML_SPIDER(scrapy.Spider):
    name = 'lxml_spider'

    start_urls = ['https://lxml.de/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'lxml'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
