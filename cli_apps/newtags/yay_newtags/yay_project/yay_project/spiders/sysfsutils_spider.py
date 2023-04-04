import scrapy
#import snoop


class SYSFSUTILS_SPIDER(scrapy.Spider):
    name = 'sysfsutils_spider'

    start_urls = ['http://linux-diag.sourceforge.net/Sysfsutils.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'sysfsutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
