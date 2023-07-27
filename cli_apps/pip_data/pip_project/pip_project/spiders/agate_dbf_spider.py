import scrapy
#import snoop


class AGATE_DBF_SPIDER(scrapy.Spider):
    name = 'agate_dbf_spider'

    start_urls = ['http://agate-dbf.readthedocs.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'agate-dbf'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
