import scrapy
#import snoop


class LIBXDAMAGE_SPIDER(scrapy.Spider):
    name = 'libxdamage_spider'

    start_urls = ['https://github.com/freedesktop/xorg-libxdamage']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libxdamage'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
