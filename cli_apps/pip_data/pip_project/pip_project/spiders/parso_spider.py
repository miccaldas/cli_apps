import scrapy
#import snoop


class PARSO_SPIDER(scrapy.Spider):
    name = 'parso_spider'

    start_urls = ['https://github.com/davidhalter/parso']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'parso'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
