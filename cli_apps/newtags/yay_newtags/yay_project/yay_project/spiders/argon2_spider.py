import scrapy
#import snoop


class ARGON2_SPIDER(scrapy.Spider):
    name = 'argon2_spider'

    start_urls = ['https://github.com/P-H-C/phc-winner-argon2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'argon2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
