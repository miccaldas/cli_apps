import scrapy
#import snoop


class OPENMPI_SPIDER(scrapy.Spider):
    name = 'openmpi_spider'

    start_urls = ['https://www.open-mpi.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'openmpi'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
