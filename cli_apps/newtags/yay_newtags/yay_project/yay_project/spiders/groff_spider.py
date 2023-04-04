import scrapy
#import snoop


class GROFF_SPIDER(scrapy.Spider):
    name = 'groff_spider'

    start_urls = ['https://www.gnu.org/software/groff/groff.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'groff'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
