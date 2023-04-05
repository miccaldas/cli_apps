import scrapy
#import snoop


class TRANSFORMERS_SPIDER(scrapy.Spider):
    name = 'transformers_spider'

    start_urls = ['https://github.com/huggingface/transformers']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'transformers'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
