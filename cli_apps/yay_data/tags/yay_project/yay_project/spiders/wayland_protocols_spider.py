import scrapy
#import snoop


class WAYLAND_PROTOCOLS_SPIDER(scrapy.Spider):
    name = 'wayland_protocols_spider'

    start_urls = ['https://wayland.freedesktop.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'wayland-protocols'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
