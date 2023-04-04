import scrapy
#import snoop


class P11_KIT_SPIDER(scrapy.Spider):
    name = 'p11_kit_spider'

    start_urls = ['https://p11-glue.freedesktop.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'p11-kit'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
