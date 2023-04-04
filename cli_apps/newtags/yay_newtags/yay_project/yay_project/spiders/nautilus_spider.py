import scrapy
#import snoop


class NAUTILUS_SPIDER(scrapy.Spider):
    name = 'nautilus_spider'

    start_urls = ['https://wiki.gnome.org/Apps/Files']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nautilus'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
