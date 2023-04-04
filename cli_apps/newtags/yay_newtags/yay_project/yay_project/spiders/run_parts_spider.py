import scrapy
#import snoop


class RUN_PARTS_SPIDER(scrapy.Spider):
    name = 'run_parts_spider'

    start_urls = ['https://packages.qa.debian.org/d/debianutils.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'run-parts'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
