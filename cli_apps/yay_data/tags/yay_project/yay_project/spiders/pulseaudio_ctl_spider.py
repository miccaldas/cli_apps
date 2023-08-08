import scrapy
#import snoop


class PULSEAUDIO_CTL_SPIDER(scrapy.Spider):
    name = 'pulseaudio_ctl_spider'

    start_urls = ['https://github.com/graysky2/pulseaudio-ctl']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pulseaudio-ctl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
