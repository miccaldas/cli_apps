import scrapy
#import snoop


class LIBHEIF_SPIDER(scrapy.Spider):
    name = 'libheif_spider'

    start_urls = ['https://github.com/strukturag/libheif']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libheif'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
