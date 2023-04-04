import scrapy
#import snoop


class GETTEXT_SPIDER(scrapy.Spider):
    name = 'gettext_spider'

    start_urls = ['https://www.gnu.org/software/gettext/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gettext'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
