import scrapy
#import snoop


class ZITA_ALSA_PCMI_SPIDER(scrapy.Spider):
    name = 'zita_alsa_pcmi_spider'

    start_urls = ['https://kokkinizita.linuxaudio.org/linuxaudio/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'zita-alsa-pcmi'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
