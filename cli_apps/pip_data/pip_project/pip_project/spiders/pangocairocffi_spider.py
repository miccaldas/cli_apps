import scrapy
#import snoop


class PANGOCAIROCFFI_SPIDER(scrapy.Spider):
    name = 'pangocairocffi_spider'

    start_urls = ['https://github.com/leifgehrmann/pangocairocffi']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pangocairocffi'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
