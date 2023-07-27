import scrapy
#import snoop


class IMPORTLIB_RESOURCES_SPIDER(scrapy.Spider):
    name = 'importlib_resources_spider'

    start_urls = ['https://github.com/python/importlib_resources']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'importlib-resources'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
