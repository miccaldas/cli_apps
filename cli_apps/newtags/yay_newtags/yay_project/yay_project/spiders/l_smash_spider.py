import scrapy
#import snoop


class L_SMASH_SPIDER(scrapy.Spider):
    name = 'l_smash_spider'

    start_urls = ['https://github.com/l-smash/l-smash']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'l-smash'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
