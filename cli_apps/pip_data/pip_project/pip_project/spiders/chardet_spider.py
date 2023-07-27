import scrapy
#import snoop


class CHARDET_SPIDER(scrapy.Spider):
    name = 'chardet_spider'

    start_urls = ['https://github.com/chardet/chardet']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'chardet'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
