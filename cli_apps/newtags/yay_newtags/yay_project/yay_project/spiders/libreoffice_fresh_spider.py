import scrapy
#import snoop


class LIBREOFFICE_FRESH_SPIDER(scrapy.Spider):
    name = 'libreoffice_fresh_spider'

    start_urls = ['https://www.libreoffice.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libreoffice-fresh'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
