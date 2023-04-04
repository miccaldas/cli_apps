import scrapy
#import snoop


class MAKE_SPIDER(scrapy.Spider):
    name = 'make_spider'

    start_urls = ['https://www.gnu.org/software/make']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'make'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
