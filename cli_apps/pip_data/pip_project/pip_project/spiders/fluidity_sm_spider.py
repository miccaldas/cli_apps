import scrapy
#import snoop


class FLUIDITY_SM_SPIDER(scrapy.Spider):
    name = 'fluidity_sm_spider'

    start_urls = ['https://github.com/nsi-iff/fluidity']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fluidity-sm'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
