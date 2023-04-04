import scrapy
#import snoop


class GLIB2_SPIDER(scrapy.Spider):
    name = 'glib2_spider'

    start_urls = ['https://wiki.gnome.org/Projects/GLib']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'glib2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
