import scrapy
#import snoop


class SOUND_THEME_FREEDESKTOP_SPIDER(scrapy.Spider):
    name = 'sound_theme_freedesktop_spider'

    start_urls = ['https://freedesktop.org/wiki/Specifications/sound-theme-spec']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sound-theme-freedesktop'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
