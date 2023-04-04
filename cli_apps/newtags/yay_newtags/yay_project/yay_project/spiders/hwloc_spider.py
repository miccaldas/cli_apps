import scrapy
#import snoop


class HWLOC_SPIDER(scrapy.Spider):
    name = 'hwloc_spider'

    start_urls = ['https://www.open-mpi.org/projects/hwloc/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'hwloc'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
