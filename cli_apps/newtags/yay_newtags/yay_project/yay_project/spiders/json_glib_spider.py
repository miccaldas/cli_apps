import scrapy
#import snoop


class JSON_GLIB_SPIDER(scrapy.Spider):
    name = 'json_glib_spider'

    start_urls = ['https://wiki.gnome.org/Projects/JsonGlib']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'json-glib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
