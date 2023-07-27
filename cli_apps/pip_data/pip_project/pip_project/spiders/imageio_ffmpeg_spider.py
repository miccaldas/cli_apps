import scrapy
#import snoop


class IMAGEIO_FFMPEG_SPIDER(scrapy.Spider):
    name = 'imageio_ffmpeg_spider'

    start_urls = ['https://github.com/imageio/imageio-ffmpeg']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'imageio-ffmpeg'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
