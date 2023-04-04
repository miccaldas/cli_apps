import scrapy
#import snoop


class PORTAUDIO_SPIDER(scrapy.Spider):
    name = 'portaudio_spider'

    start_urls = ['https://github.com/portaudio/portaudio/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'portaudio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
