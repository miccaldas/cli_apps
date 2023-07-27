import scrapy
#import snoop


class LIBFDT_SPIDER(scrapy.Spider):
    name = 'libfdt_spider'

    start_urls = ['https://git.kernel.org/pub/scm/utils/dtc/dtc.git']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libfdt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
