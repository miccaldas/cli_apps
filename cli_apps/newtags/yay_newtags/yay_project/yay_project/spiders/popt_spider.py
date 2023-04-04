import scrapy
#import snoop


class POPT_SPIDER(scrapy.Spider):
    name = 'popt_spider'

    start_urls = ['https://github.com/rpm-software-management/popt']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'popt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
