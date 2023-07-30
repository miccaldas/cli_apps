import scrapy
#import snoop


class GIFTOOL_SPIDER(scrapy.Spider):
    name = 'giftool_spider'

    start_urls = ['https://github.com/mattdesl/giftool/blob/master/README.md']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'giftool'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
