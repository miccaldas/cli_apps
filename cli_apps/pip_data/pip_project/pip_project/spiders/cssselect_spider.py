import scrapy
#import snoop


class CSSSELECT_SPIDER(scrapy.Spider):
    name = 'cssselect_spider'

    start_urls = ['https://github.com/scrapy/cssselect']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cssselect'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
