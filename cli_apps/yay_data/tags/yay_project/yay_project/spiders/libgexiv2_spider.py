import scrapy
#import snoop


class LIBGEXIV2_SPIDER(scrapy.Spider):
    name = 'libgexiv2_spider'

    start_urls = ['https://wiki.gnome.org/Projects/gexiv2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libgexiv2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
