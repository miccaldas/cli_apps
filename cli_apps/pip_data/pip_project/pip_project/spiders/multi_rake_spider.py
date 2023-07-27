import scrapy
#import snoop


class MULTI_RAKE_SPIDER(scrapy.Spider):
    name = 'multi_rake_spider'

    start_urls = ['https://github.com/vgrabovets/multi_rake']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'multi-rake'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
