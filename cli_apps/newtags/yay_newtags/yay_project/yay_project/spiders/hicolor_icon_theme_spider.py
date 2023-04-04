import scrapy
#import snoop


class HICOLOR_ICON_THEME_SPIDER(scrapy.Spider):
    name = 'hicolor_icon_theme_spider'

    start_urls = ['https://www.freedesktop.org/wiki/Software/icon-theme/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'hicolor-icon-theme'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
