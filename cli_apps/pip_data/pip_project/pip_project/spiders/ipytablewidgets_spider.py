import scrapy
#import snoop


class IPYTABLEWIDGETS_SPIDER(scrapy.Spider):
    name = 'ipytablewidgets_spider'

    start_urls = ['https://github.com/progressivis/ipytablewidgets']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ipytablewidgets'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
