import scrapy
#import snoop


class SED_SPIDER(scrapy.Spider):
    name = 'sed_spider'

    start_urls = ['https://www.gnu.org/software/sed/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sed'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
