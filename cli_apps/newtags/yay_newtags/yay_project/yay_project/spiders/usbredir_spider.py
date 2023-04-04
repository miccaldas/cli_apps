import scrapy
#import snoop


class USBREDIR_SPIDER(scrapy.Spider):
    name = 'usbredir_spider'

    start_urls = ['https://www.spice-space.org/usbredir.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'usbredir'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
