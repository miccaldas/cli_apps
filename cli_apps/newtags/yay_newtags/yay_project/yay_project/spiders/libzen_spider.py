import scrapy
#import snoop


class LIBZEN_SPIDER(scrapy.Spider):
    name = 'libzen_spider'

    start_urls = ['https://mediaarea.net']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libzen'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
