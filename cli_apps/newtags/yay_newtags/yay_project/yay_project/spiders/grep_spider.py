import scrapy
#import snoop


class GREP_SPIDER(scrapy.Spider):
    name = 'grep_spider'

    start_urls = ['https://www.gnu.org/software/grep/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'grep'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
