import scrapy
#import snoop


class TERMINUS_FONT_SPIDER(scrapy.Spider):
    name = 'terminus_font_spider'

    start_urls = ['http://terminus-font.sourceforge.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'terminus-font'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
