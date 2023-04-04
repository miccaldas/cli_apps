import scrapy
#import snoop


class JSON_C_SPIDER(scrapy.Spider):
    name = 'json_c_spider'

    start_urls = ['https://github.com/json-c/json-c/wiki']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'json-c'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
