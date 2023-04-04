import scrapy
#import snoop


class CRACKLIB_SPIDER(scrapy.Spider):
    name = 'cracklib_spider'

    start_urls = ['https://github.com/cracklib/cracklib']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cracklib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
