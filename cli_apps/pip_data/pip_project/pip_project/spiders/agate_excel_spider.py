import scrapy
#import snoop


class AGATE_EXCEL_SPIDER(scrapy.Spider):
    name = 'agate_excel_spider'

    start_urls = ['http://agate-excel.readthedocs.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'agate-excel'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
