import scrapy
#import snoop


class PVDISPLAY_SPIDER(scrapy.Spider):
    name = 'pvdisplay_spider'

    start_urls = ['https://linux.die.net/man/8/pvdisplay']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pvdisplay'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
