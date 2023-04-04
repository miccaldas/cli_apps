import scrapy
#import snoop


class DBUS_SPIDER(scrapy.Spider):
    name = 'dbus_spider'

    start_urls = ['https://wiki.freedesktop.org/www/Software/dbus/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dbus'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
