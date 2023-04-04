import scrapy
#import snoop


class RAV1E_SPIDER(scrapy.Spider):
    name = 'rav1e_spider'

    start_urls = ['https://github.com/xiph/rav1e/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'rav1e'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
