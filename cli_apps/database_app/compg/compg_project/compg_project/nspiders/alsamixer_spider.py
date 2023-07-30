import scrapy
#import snoop


class ALSAMIXER_SPIDER(scrapy.Spider):
    name = 'alsamixer_spider'

    start_urls = ['https://linux.die.net/man/1/alsamixer']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'alsamixer'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
