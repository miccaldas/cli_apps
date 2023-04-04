import scrapy
#import snoop


class LIBOMXIL_BELLAGIO_SPIDER(scrapy.Spider):
    name = 'libomxil_bellagio_spider'

    start_urls = ['http://omxil.sourceforge.net']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libomxil-bellagio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
