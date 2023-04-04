import scrapy
#import snoop


class DKMS_SPIDER(scrapy.Spider):
    name = 'dkms_spider'

    start_urls = ['https://github.com/dell/dkms']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dkms'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
