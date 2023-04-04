import scrapy
#import snoop


class PBZIP2_SPIDER(scrapy.Spider):
    name = 'pbzip2_spider'

    start_urls = ['https://linux.die.net/man/1/pbzip2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pbzip2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
