import scrapy
#import snoop


class LIBPLACEBO_SPIDER(scrapy.Spider):
    name = 'libplacebo_spider'

    start_urls = ['https://github.com/haasn/libplacebo']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libplacebo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
