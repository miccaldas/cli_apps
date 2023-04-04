import scrapy
#import snoop


class BOTAN_SPIDER(scrapy.Spider):
    name = 'botan_spider'

    start_urls = ['https://botan.randombit.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'botan'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
