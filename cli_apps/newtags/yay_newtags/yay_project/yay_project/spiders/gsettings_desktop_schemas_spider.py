import scrapy
#import snoop


class GSETTINGS_DESKTOP_SCHEMAS_SPIDER(scrapy.Spider):
    name = 'gsettings_desktop_schemas_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/gsettings-desktop-schemas']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gsettings-desktop-schemas'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
