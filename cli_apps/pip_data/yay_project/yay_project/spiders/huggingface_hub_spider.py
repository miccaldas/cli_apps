import scrapy
#import snoop


class HUGGINGFACE_HUB_SPIDER(scrapy.Spider):
    name = 'huggingface_hub_spider'

    start_urls = ['https://github.com/huggingface/huggingface_hub']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'huggingface-hub'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
