import scrapy
#import snoop


class GDBM_SPIDER(scrapy.Spider):
    name = 'gdbm_spider'

    start_urls = ['https://www.gnu.org/software/gdbm/gdbm.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gdbm'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
