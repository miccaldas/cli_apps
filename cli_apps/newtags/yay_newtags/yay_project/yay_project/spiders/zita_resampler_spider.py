import scrapy
#import snoop


class ZITA_RESAMPLER_SPIDER(scrapy.Spider):
    name = 'zita_resampler_spider'

    start_urls = ['https://kokkinizita.linuxaudio.org/linuxaudio']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'zita-resampler'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
