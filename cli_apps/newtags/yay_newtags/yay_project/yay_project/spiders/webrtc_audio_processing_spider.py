import scrapy
#import snoop


class WEBRTC_AUDIO_PROCESSING_SPIDER(scrapy.Spider):
    name = 'webrtc_audio_processing_spider'

    start_urls = ['https://freedesktop.org/software/pulseaudio/webrtc-audio-processing/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'webrtc-audio-processing'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
