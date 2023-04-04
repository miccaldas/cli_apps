import scrapy
#import snoop


class LSOF_SPIDER(scrapy.Spider):
    name = 'lsof_spider'

    start_urls = ['https://github.com/lsof-org/lsof']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'lsof'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
