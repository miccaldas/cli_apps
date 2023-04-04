import scrapy
#import snoop


class SLANG_SPIDER(scrapy.Spider):
    name = 'slang_spider'

    start_urls = ['https://www.jedsoft.org/slang/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'slang'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results