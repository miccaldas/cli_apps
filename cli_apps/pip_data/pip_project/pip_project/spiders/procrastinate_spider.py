import scrapy
#import snoop


class PROCRASTINATE_SPIDER(scrapy.Spider):
    name = 'procrastinate_spider'

    start_urls = ['https://procrastinate.readthedocs.io/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'procrastinate'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
