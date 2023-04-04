import scrapy
#import snoop


class BINUTILS_SPIDER(scrapy.Spider):
    name = 'binutils_spider'

    start_urls = ['https://www.gnu.org/software/binutils/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'binutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
