import scrapy
#import snoop


class LIBACCOUNTS_GLIB_SPIDER(scrapy.Spider):
    name = 'libaccounts_glib_spider'

    start_urls = ['https://gitlab.com/accounts-sso/libaccounts-glib']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libaccounts-glib'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
