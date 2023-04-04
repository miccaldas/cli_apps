import scrapy
#import snoop


class PATCH_SPIDER(scrapy.Spider):
    name = 'patch_spider'

    start_urls = ['https://www.gnu.org/software/patch/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'patch'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
