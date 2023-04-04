import scrapy
#import snoop


class LIBURING_SPIDER(scrapy.Spider):
    name = 'liburing_spider'

    start_urls = ['https://git.kernel.dk/cgit/liburing/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'liburing'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
