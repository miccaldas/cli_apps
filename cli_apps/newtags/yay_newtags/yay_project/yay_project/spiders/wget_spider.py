import scrapy
#import snoop


class WGET_SPIDER(scrapy.Spider):
    name = 'wget_spider'

    start_urls = ['https://www.gnu.org/software/wget/wget.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'wget'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
