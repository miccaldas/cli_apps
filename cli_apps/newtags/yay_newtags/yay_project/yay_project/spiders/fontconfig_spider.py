import scrapy
#import snoop


class FONTCONFIG_SPIDER(scrapy.Spider):
    name = 'fontconfig_spider'

    start_urls = ['https://www.freedesktop.org/wiki/Software/fontconfig/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fontconfig'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
