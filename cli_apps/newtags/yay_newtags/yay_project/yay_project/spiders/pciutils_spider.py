import scrapy
#import snoop


class PCIUTILS_SPIDER(scrapy.Spider):
    name = 'pciutils_spider'

    start_urls = ['https://mj.ucw.cz/sw/pciutils/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pciutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
