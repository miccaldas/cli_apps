import scrapy
#import snoop


class TRACKER3_SPIDER(scrapy.Spider):
    name = 'tracker3_spider'

    start_urls = ['https://wiki.gnome.org/Projects/Tracker']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tracker3'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
