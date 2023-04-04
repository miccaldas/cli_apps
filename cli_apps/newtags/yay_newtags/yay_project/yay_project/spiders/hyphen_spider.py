import scrapy
#import snoop


class HYPHEN_SPIDER(scrapy.Spider):
    name = 'hyphen_spider'

    start_urls = ['https://hunspell.sf.net']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'hyphen'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
