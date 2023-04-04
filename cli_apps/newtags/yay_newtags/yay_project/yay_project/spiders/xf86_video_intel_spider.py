import scrapy
#import snoop


class XF86_VIDEO_INTEL_SPIDER(scrapy.Spider):
    name = 'xf86_video_intel_spider'

    start_urls = ['https://01.org/linuxgraphics']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xf86-video-intel'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
