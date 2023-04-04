import scrapy
#import snoop


class MICRO_SPIDER(scrapy.Spider):
    name = 'micro_spider'

    start_urls = ['https://micro-editor.github.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'micro'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
