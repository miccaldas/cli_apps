import scrapy
#import snoop


class HYPERFRAME_SPIDER(scrapy.Spider):
    name = 'hyperframe_spider'

    start_urls = ['https://github.com/python-hyper/hyperframe/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'hyperframe'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
