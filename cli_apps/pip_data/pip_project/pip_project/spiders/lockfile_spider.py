import scrapy
#import snoop


class LOCKFILE_SPIDER(scrapy.Spider):
    name = 'lockfile_spider'

    start_urls = ['http://launchpad.net/pylockfile']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'lockfile'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
