import scrapy
#import snoop


class LIBATASMART_SPIDER(scrapy.Spider):
    name = 'libatasmart_spider'

    start_urls = ['http://0pointer.de/blog/projects/being-smart.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libatasmart'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
