import scrapy
#import snoop


class ARGON2_CFFI_BINDINGS_SPIDER(scrapy.Spider):
    name = 'argon2_cffi_bindings_spider'

    start_urls = ['https://github.com/hynek/argon2-cffi-bindings']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'argon2-cffi-bindings'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
