import scrapy
#import snoop


class GPROF2DOT_SPIDER(scrapy.Spider):
    name = 'gprof2dot_spider'

    start_urls = ['https://github.com/jrfonseca/gprof2dot']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gprof2dot'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
