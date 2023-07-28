import scrapy
#import snoop


class JSONSCHEMA_SPECIFICATIONS_SPIDER(scrapy.Spider):
    name = 'jsonschema_specifications_spider'

    start_urls = ['NA']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jsonschema-specifications'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results