import scrapy
#import snoop


class TEXINFO_SPIDER(scrapy.Spider):
    name = 'texinfo_spider'

    start_urls = ['https://www.gnu.org/software/texinfo/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'texinfo'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
