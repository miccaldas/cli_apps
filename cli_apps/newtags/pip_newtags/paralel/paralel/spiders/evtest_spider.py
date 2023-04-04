import scrapy
#import snoop


class EVTEST_SPIDER(scrapy.Spider):
    name = 'evtest_spider'

    start_urls = ['https://manpages.ubuntu.com/manpages/trusty/man1/evtest.1.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'evtest'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
