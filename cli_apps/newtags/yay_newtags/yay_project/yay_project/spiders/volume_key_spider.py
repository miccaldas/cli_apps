import scrapy
#import snoop


class VOLUME_KEY_SPIDER(scrapy.Spider):
    name = 'volume_key_spider'

    start_urls = ['https://pagure.io/volume_key']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'volume_key'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
