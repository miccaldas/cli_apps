import scrapy
#import snoop


class ITEMADAPTER_SPIDER(scrapy.Spider):
    name = 'itemadapter_spider'

    start_urls = ['https://github.com/scrapy/itemadapter']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'itemadapter'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
