import scrapy
#import snoop


class XORG_FONTS_75DPI_SPIDER(scrapy.Spider):
    name = 'xorg_fonts_75dpi_spider'

    start_urls = ['https://github.com/freedesktop/xorg-fonts-75dpi']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-fonts-75dpi'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
