import scrapy
#import snoop


class MEDIA_PLAYER_INFO_SPIDER(scrapy.Spider):
    name = 'media_player_info_spider'

    start_urls = ['https://www.freedesktop.org/wiki/Software/media-player-info/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'media-player-info'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
