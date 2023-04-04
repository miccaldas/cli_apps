import scrapy
#import snoop


class YAJL_SPIDER(scrapy.Spider):
    name = 'yajl_spider'

    start_urls = ['https://lloyd.github.com/yajl/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'yajl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
