import scrapy
#import snoop


class TESTDISK_SPIDER(scrapy.Spider):
    name = 'testdisk_spider'

    start_urls = ['https://www.cgsecurity.org/index.html?testdisk.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'testdisk'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
