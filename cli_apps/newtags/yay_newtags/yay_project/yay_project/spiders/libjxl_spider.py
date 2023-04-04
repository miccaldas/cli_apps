import scrapy
#import snoop


class LIBJXL_SPIDER(scrapy.Spider):
    name = 'libjxl_spider'

    start_urls = ['https://jpeg.org/jpegxl/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libjxl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
