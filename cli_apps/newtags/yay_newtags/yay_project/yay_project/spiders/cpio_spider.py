import scrapy
#import snoop


class CPIO_SPIDER(scrapy.Spider):
    name = 'cpio_spider'

    start_urls = ['https://www.gnu.org/software/cpio']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cpio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
