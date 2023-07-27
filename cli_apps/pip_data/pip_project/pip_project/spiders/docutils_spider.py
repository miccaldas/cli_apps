import scrapy
#import snoop


class DOCUTILS_SPIDER(scrapy.Spider):
    name = 'docutils_spider'

    start_urls = ['https://docutils.sourceforge.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'docutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
