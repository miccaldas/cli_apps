import scrapy
#import snoop


class BACKCALL_SPIDER(scrapy.Spider):
    name = 'backcall_spider'

    start_urls = ['https://github.com/takluyver/backcall']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'backcall'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
