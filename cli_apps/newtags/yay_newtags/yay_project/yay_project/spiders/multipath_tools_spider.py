import scrapy
#import snoop


class MULTIPATH_TOOLS_SPIDER(scrapy.Spider):
    name = 'multipath_tools_spider'

    start_urls = ['https://github.com/opensvc/multipath-tools']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'multipath-tools'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
