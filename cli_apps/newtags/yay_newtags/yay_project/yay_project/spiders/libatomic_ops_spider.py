import scrapy
#import snoop


class LIBATOMIC_OPS_SPIDER(scrapy.Spider):
    name = 'libatomic_ops_spider'

    start_urls = ['https://github.com/ivmai/libatomic_ops']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libatomic_ops'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
