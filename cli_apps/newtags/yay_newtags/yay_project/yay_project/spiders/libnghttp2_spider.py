import scrapy
#import snoop


class LIBNGHTTP2_SPIDER(scrapy.Spider):
    name = 'libnghttp2_spider'

    start_urls = ['https://nghttp2.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libnghttp2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
