import scrapy
#import snoop


class PULSEAUDIO_ALSA_SPIDER(scrapy.Spider):
    name = 'pulseaudio_alsa_spider'

    start_urls = ['https://www.alsa-project.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pulseaudio-alsa'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
