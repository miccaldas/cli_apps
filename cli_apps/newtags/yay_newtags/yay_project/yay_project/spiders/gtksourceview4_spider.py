import scrapy
#import snoop


class GTKSOURCEVIEW4_SPIDER(scrapy.Spider):
    name = 'gtksourceview4_spider'

    start_urls = ['https://wiki.gnome.org/Projects/GtkSourceView']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gtksourceview4'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
