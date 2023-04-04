import scrapy
#import snoop


class LIBLANGTAG_SPIDER(scrapy.Spider):
    name = 'liblangtag_spider'

    start_urls = ['https://bitbucket.org/tagoh/liblangtag/wiki/Home']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'liblangtag'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
