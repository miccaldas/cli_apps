import scrapy
#import snoop


class MINIZIP_SPIDER(scrapy.Spider):
    name = 'minizip_spider'

    start_urls = ['https://www.zlib.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'minizip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
