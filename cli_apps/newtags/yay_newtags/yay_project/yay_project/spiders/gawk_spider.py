import scrapy
#import snoop


class GAWK_SPIDER(scrapy.Spider):
    name = 'gawk_spider'

    start_urls = ['https://www.gnu.org/software/gawk/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gawk'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
