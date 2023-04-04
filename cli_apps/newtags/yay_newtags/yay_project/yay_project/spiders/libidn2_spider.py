import scrapy
#import snoop


class LIBIDN2_SPIDER(scrapy.Spider):
    name = 'libidn2_spider'

    start_urls = ['https://www.gnu.org/software/libidn/#libidn2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libidn2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
