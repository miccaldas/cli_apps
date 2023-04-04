import scrapy
#import snoop


class ATTR_SPIDER(scrapy.Spider):
    name = 'attr_spider'

    start_urls = ['https://savannah.nongnu.org/projects/attr']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'attr'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
