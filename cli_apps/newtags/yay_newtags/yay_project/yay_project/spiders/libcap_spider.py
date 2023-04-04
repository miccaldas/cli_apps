import scrapy
#import snoop


class LIBCAP_SPIDER(scrapy.Spider):
    name = 'libcap_spider'

    start_urls = ['https://sites.google.com/site/fullycapable/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libcap'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
