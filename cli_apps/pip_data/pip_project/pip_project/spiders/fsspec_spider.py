import scrapy
#import snoop


class FSSPEC_SPIDER(scrapy.Spider):
    name = 'fsspec_spider'

    start_urls = ['http://github.com/fsspec/filesystem_spec']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'fsspec'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
