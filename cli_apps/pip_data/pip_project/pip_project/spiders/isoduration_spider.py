import scrapy
#import snoop


class ISODURATION_SPIDER(scrapy.Spider):
    name = 'isoduration_spider'

    start_urls = ['https://github.com/bolsote/isoduration']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'isoduration'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
