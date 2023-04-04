import scrapy
#import snoop


class RE2_SPIDER(scrapy.Spider):
    name = 're2_spider'

    start_urls = ['https://github.com/google/re2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 're2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
