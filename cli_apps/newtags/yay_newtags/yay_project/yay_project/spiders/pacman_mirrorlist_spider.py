import scrapy
#import snoop


class PACMAN_MIRRORLIST_SPIDER(scrapy.Spider):
    name = 'pacman_mirrorlist_spider'

    start_urls = ['https://www.archlinux.org/mirrorlist/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pacman-mirrorlist'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
