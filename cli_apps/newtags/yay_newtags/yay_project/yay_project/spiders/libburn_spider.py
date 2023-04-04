import scrapy
#import snoop


class LIBBURN_SPIDER(scrapy.Spider):
    name = 'libburn_spider'

    start_urls = ['https://dev.lovelyhq.com/libburnia']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libburn'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
