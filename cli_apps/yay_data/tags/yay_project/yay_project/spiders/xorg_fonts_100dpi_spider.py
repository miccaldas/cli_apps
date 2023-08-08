import scrapy
#import snoop


class XORG_FONTS_100DPI_SPIDER(scrapy.Spider):
    name = 'xorg_fonts_100dpi_spider'

    start_urls = ['https://github.com/freedesktop/xorg-fonts-100dpi']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xorg-fonts-100dpi'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
