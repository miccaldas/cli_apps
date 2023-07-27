import scrapy
#import snoop


class JSONPOINTER_SPIDER(scrapy.Spider):
    name = 'jsonpointer_spider'

    start_urls = ['https://github.com/stefankoegl/python-json-pointer']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jsonpointer'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
