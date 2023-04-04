import scrapy
#import snoop


class GUPNP_IGD_SPIDER(scrapy.Spider):
    name = 'gupnp_igd_spider'

    start_urls = ['https://wiki.gnome.org/Projects/GUPnP']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gupnp-igd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
