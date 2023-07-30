import scrapy
#import snoop


class PAMSTRETCH_GEN_SPIDER(scrapy.Spider):
    name = 'pamstretch_gen_spider'

    start_urls = ['https://netpbm.sourceforge.net/doc/pamstretch-gen.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pamstretch-gen'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
