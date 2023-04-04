import scrapy
#import snoop


class ENCHANT_SPIDER(scrapy.Spider):
    name = 'enchant_spider'

    start_urls = ['https://abiword.github.io/enchant/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'enchant'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
