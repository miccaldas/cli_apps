import scrapy
#import snoop


class CDRSKIN_SPIDER(scrapy.Spider):
    name = 'cdrskin_spider'

    start_urls = ['https://linux.die.net/man/1/cdrskin']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cdrskin'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
