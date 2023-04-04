import scrapy
#import snoop


class XF86_VIDEO_VMWARE_SPIDER(scrapy.Spider):
    name = 'xf86_video_vmware_spider'

    start_urls = ['https://github.com/freedesktop/xorg-xf86-video-vmware']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xf86-video-vmware'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
