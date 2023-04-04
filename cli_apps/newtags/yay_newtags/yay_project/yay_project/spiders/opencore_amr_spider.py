import scrapy
#import snoop


class OPENCORE_AMR_SPIDER(scrapy.Spider):
    name = 'opencore_amr_spider'

    start_urls = ['https://sourceforge.net/projects/opencore-amr/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'opencore-amr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
