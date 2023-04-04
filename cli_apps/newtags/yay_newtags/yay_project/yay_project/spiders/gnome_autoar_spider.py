import scrapy
#import snoop


class GNOME_AUTOAR_SPIDER(scrapy.Spider):
    name = 'gnome_autoar_spider'

    start_urls = ['https://wiki.gnome.org/TingweiLan/GSoC2013Final']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gnome-autoar'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
