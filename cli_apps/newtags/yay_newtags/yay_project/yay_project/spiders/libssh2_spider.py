import scrapy
#import snoop


class LIBSSH2_SPIDER(scrapy.Spider):
    name = 'libssh2_spider'

    start_urls = ['https://www.libssh2.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libssh2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
