import scrapy
#import snoop


class THUNDERBIRD_SPIDER(scrapy.Spider):
    name = 'thunderbird_spider'

    start_urls = ['https://www.mozilla.org/thunderbird/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'thunderbird'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
