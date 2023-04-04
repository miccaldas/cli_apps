import scrapy
#import snoop


class LIBWEBP_SPIDER(scrapy.Spider):
    name = 'libwebp_spider'

    start_urls = ['https://developers.google.com/speed/webp/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libwebp'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
