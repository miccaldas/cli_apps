import scrapy
#import snoop


class JARACO_CLASSES_SPIDER(scrapy.Spider):
    name = 'jaraco_classes_spider'

    start_urls = ['https://github.com/jaraco/jaraco.classes']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jaraco.classes'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
