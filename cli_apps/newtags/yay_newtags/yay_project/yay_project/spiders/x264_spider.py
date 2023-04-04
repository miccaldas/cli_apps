import scrapy
#import snoop


class X264_SPIDER(scrapy.Spider):
    name = 'x264_spider'

    start_urls = ['https://www.videolan.org/developers/x264.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'x264'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
