import scrapy
#import snoop


class NCURSES_SPIDER(scrapy.Spider):
    name = 'ncurses_spider'

    start_urls = ['https://invisible-island.net/ncurses/ncurses.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ncurses'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
