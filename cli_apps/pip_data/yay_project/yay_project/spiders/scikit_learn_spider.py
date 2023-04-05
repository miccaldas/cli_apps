import scrapy
#import snoop


class SCIKIT_LEARN_SPIDER(scrapy.Spider):
    name = 'scikit_learn_spider'

    start_urls = ['http://scikit-learn.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'scikit-learn'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
