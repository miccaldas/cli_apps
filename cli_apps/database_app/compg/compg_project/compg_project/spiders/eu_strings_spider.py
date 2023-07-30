import scrapy
#import snoop


class EU_STRINGS_SPIDER(scrapy.Spider):
    name = 'eu_strings_spider'

    start_urls = ['https://helpmanual.io/help/eu-strings/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'eu-strings'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
