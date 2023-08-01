import scrapy
#import snoop


class CDDA_PLAYER_SPIDER(scrapy.Spider):
    name = 'cdda_player_spider'

    start_urls = ['https://manpages.debian.org/testing/libcdio-utils/cdda-player.1.en.html']

    #@snoop
    def parse(self, response):
        srch_text = response.xpath("///*[@id='content']/div[2]/div/div/section[3]/p/text()").get()

        srch_description = response.xpath("///*[@id='content']/div[2]/div/div/section[1]/p/text()").get()
        name = 'cdda-player'

        lsts = srch_text + srch_description
        results = {'name': name, 'content': lsts}
        yield results
