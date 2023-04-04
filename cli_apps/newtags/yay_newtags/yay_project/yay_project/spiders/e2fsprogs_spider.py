import scrapy
#import snoop


class E2FSPROGS_SPIDER(scrapy.Spider):
    name = 'e2fsprogs_spider'

    start_urls = ['http://e2fsprogs.sourceforge.net']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'e2fsprogs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results