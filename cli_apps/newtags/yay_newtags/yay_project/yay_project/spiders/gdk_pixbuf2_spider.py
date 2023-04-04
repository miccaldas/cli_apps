import scrapy
#import snoop


class GDK_PIXBUF2_SPIDER(scrapy.Spider):
    name = 'gdk_pixbuf2_spider'

    start_urls = ['https://wiki.gnome.org/Projects/GdkPixbuf']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gdk-pixbuf2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
