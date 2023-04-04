import scrapy
#import snoop


class LIBIPTCDATA_SPIDER(scrapy.Spider):
    name = 'libiptcdata_spider'

    start_urls = ['http://libiptcdata.sourceforge.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libiptcdata'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
