import scrapy
#import snoop


class EXIV2_SPIDER(scrapy.Spider):
    name = 'exiv2_spider'

    start_urls = ['https://exiv2.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'exiv2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
