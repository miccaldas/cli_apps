import scrapy
#import snoop


class HYPERLINK_SPIDER(scrapy.Spider):
    name = 'hyperlink_spider'

    start_urls = ['https://github.com/python-hyper/hyperlink']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'hyperlink'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
