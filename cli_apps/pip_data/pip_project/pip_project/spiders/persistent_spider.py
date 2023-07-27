import scrapy
#import snoop


class PERSISTENT_SPIDER(scrapy.Spider):
    name = 'persistent_spider'

    start_urls = ['https://github.com/zopefoundation/persistent/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'persistent'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
