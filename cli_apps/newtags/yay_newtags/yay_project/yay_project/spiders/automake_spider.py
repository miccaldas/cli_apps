import scrapy
#import snoop


class AUTOMAKE_SPIDER(scrapy.Spider):
    name = 'automake_spider'

    start_urls = ['https://www.gnu.org/software/automake']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'automake'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
