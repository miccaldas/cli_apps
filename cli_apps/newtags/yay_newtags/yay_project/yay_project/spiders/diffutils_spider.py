import scrapy
#import snoop


class DIFFUTILS_SPIDER(scrapy.Spider):
    name = 'diffutils_spider'

    start_urls = ['https://www.gnu.org/software/diffutils']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'diffutils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
