import scrapy
#import snoop


class CHARSET_NORMALIZER_SPIDER(scrapy.Spider):
    name = 'charset_normalizer_spider'

    start_urls = ['https://github.com/Ousret/charset_normalizer']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'charset-normalizer'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
