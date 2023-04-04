import scrapy
#import snoop


class ORC_SPIDER(scrapy.Spider):
    name = 'orc_spider'

    start_urls = ['https://gitlab.freedesktop.org/gstreamer/orc']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'orc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
