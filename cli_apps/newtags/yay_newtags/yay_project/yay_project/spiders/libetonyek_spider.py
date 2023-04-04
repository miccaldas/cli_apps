import scrapy
#import snoop


class LIBETONYEK_SPIDER(scrapy.Spider):
    name = 'libetonyek_spider'

    start_urls = ['https://wiki.documentfoundation.org/DLP/Libraries/libetonyek']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libetonyek'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
