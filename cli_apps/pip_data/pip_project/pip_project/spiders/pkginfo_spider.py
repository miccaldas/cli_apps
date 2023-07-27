import scrapy
#import snoop


class PKGINFO_SPIDER(scrapy.Spider):
    name = 'pkginfo_spider'

    start_urls = ['https://code.launchpad.net/~tseaver/pkginfo/trunk']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pkginfo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
