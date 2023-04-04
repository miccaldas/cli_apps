import scrapy
#import snoop


class VTE3_SPIDER(scrapy.Spider):
    name = 'vte3_spider'

    start_urls = ['https://wiki.gnome.org/Apps/Terminal/VTE']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'vte3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
