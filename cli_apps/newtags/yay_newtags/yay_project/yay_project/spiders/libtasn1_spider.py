import scrapy
#import snoop


class LIBTASN1_SPIDER(scrapy.Spider):
    name = 'libtasn1_spider'

    start_urls = ['https://www.gnu.org/software/libtasn1/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libtasn1'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
