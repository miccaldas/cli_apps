import scrapy
#import snoop


class GOBJECT_INTROSPECTION_RUNTIME_SPIDER(scrapy.Spider):
    name = 'gobject_introspection_runtime_spider'

    start_urls = ['https://wiki.gnome.org/Projects/GObjectIntrospection']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gobject-introspection-runtime'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
