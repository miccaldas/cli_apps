import scrapy
#import snoop


class LIBSODIUM_SPIDER(scrapy.Spider):
    name = 'libsodium_spider'

    start_urls = ['https://github.com/jedisct1/libsodium']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsodium'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
