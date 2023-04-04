import scrapy
#import snoop


class LIBOPENMPT_SPIDER(scrapy.Spider):
    name = 'libopenmpt_spider'

    start_urls = ['https://lib.openmpt.org/libopenmpt/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libopenmpt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
