import scrapy
#import snoop


class CRYPTSETUP_SPIDER(scrapy.Spider):
    name = 'cryptsetup_spider'

    start_urls = ['https://gitlab.com/cryptsetup/cryptsetup/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cryptsetup'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
