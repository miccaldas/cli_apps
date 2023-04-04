import scrapy
#import snoop


class PACMAN_CONTRIB_SPIDER(scrapy.Spider):
    name = 'pacman_contrib_spider'

    start_urls = ['https://gitlab.archlinux.org/pacman/pacman-contrib']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pacman-contrib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
