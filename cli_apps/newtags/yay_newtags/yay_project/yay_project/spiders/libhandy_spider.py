import scrapy
#import snoop


class LIBHANDY_SPIDER(scrapy.Spider):
    name = 'libhandy_spider'

    start_urls = ['https://gitlab.gnome.org/GNOME/libhandy']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libhandy'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
