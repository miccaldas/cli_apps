import scrapy
#import snoop


class JIEBA_SPIDER(scrapy.Spider):
    name = 'jieba_spider'

    start_urls = ['https://github.com/fxsjy/jieba']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jieba'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
