import scrapy
#import snoop


class LIBSOUP3_SPIDER(scrapy.Spider):
    name = 'libsoup3_spider'

    start_urls = ['https://wiki.gnome.org/Projects/libsoup']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsoup3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results