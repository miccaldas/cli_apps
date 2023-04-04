import scrapy
#import snoop


class ROFI_GREENCLIP_SPIDER(scrapy.Spider):
    name = 'rofi_greenclip_spider'

    start_urls = ['https://github.com/erebe/greenclip']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'rofi-greenclip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
