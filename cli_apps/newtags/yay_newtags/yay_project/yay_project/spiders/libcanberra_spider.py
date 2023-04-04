import scrapy
#import snoop


class LIBCANBERRA_SPIDER(scrapy.Spider):
    name = 'libcanberra_spider'

    start_urls = ['https://0pointer.net/lennart/projects/libcanberra/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcanberra'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
