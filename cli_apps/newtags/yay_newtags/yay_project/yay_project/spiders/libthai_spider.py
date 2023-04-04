import scrapy
#import snoop


class LIBTHAI_SPIDER(scrapy.Spider):
    name = 'libthai_spider'

    start_urls = ['https://linux.thai.net/projects/libthai']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libthai'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
