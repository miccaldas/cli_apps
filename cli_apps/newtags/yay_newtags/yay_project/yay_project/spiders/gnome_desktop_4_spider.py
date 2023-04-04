import scrapy
#import snoop


class GNOME_DESKTOP_4_SPIDER(scrapy.Spider):
    name = 'gnome_desktop_4_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/gnome-desktop']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gnome-desktop-4'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
