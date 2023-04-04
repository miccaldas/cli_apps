import scrapy
#import snoop


class KITTY_TERMINFO_SPIDER(scrapy.Spider):
    name = 'kitty_terminfo_spider'

    start_urls = ['https://github.com/kovidgoyal/kitty']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'kitty-terminfo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
