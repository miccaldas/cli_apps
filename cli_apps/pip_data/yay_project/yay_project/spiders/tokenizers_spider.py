import scrapy
#import snoop


class TOKENIZERS_SPIDER(scrapy.Spider):
    name = 'tokenizers_spider'

    start_urls = ['https://github.com/huggingface/tokenizers']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tokenizers'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
