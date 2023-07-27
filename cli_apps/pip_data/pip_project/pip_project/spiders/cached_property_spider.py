import scrapy
#import snoop


class CACHED_PROPERTY_SPIDER(scrapy.Spider):
    name = 'cached_property_spider'

    start_urls = ['https://github.com/pydanny/cached-property']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cached-property'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
