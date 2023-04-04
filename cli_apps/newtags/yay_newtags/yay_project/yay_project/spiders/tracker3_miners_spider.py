import scrapy
#import snoop


class TRACKER3_MINERS_SPIDER(scrapy.Spider):
    name = 'tracker3_miners_spider'

    start_urls = ['https://wiki.gnome.org/Projects/Tracker']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'tracker3-miners'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
