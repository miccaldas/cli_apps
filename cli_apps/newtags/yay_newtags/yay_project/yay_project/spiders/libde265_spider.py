import scrapy
#import snoop


class LIBDE265_SPIDER(scrapy.Spider):
    name = 'libde265_spider'

    start_urls = ['https://github.com/strukturag/libde265']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libde265'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
