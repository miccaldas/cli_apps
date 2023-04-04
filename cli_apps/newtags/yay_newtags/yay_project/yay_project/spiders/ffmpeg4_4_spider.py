import scrapy
#import snoop


class FFMPEG4_4_SPIDER(scrapy.Spider):
    name = 'ffmpeg4_4_spider'

    start_urls = ['https://ffmpeg.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ffmpeg4.4'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
