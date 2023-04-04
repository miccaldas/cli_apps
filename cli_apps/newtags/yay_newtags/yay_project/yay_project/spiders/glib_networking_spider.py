import scrapy
#import snoop


class GLIB_NETWORKING_SPIDER(scrapy.Spider):
    name = 'glib_networking_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/glib-networking']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'glib-networking'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
