import scrapy
#import snoop


class DOUBLE_CONVERSION_SPIDER(scrapy.Spider):
    name = 'double_conversion_spider'

    start_urls = ['https://github.com/google/double-conversion']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'double-conversion'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
