import scrapy
#import snoop


class OVERRIDES_SPIDER(scrapy.Spider):
    name = 'overrides_spider'

    start_urls = ['https://github.com/mkorpela/overrides']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'overrides'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
