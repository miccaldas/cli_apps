import scrapy
#import snoop


class ADWAITA_ICON_THEME_SPIDER(scrapy.Spider):
    name = 'adwaita_icon_theme_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/adwaita-icon-theme']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'adwaita-icon-theme'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
