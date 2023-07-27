import scrapy
#import snoop


class JSON5_SPIDER(scrapy.Spider):
    name = 'json5_spider'

    start_urls = ['https://github.com/dpranke/pyjson5']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'json5'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
