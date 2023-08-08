import scrapy
#import snoop


class DBUS_GLIB_SPIDER(scrapy.Spider):
    name = 'dbus_glib_spider'

    start_urls = ['https://www.freedesktop.org/wiki/Software/dbus/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dbus-glib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
