import scrapy
#import snoop


class ALIVE_PROGRESS_SPIDER(scrapy.Spider):
    name = 'alive_progress_spider'

    start_urls = ['https://github.com/rsalmei/alive-progress']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'alive-progress'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
