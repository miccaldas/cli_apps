import scrapy
#import snoop


class POWERLINE_FONTS_SPIDER(scrapy.Spider):
    name = 'powerline_fonts_spider'

    start_urls = ['https://github.com/powerline/powerline']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'powerline-fonts'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
