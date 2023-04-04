import scrapy
#import snoop


class GPERFTOOLS_SPIDER(scrapy.Spider):
    name = 'gperftools_spider'

    start_urls = ['https://github.com/gperftools/gperftools']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gperftools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
