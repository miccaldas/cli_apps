import scrapy
#import snoop


class ELFUTILS_SPIDER(scrapy.Spider):
    name = 'elfutils_spider'

    start_urls = ['https://sourceware.org/elfutils/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'elfutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
