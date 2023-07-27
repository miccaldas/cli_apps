import scrapy
#import snoop


class MARKDOWNIFY_SPIDER(scrapy.Spider):
    name = 'markdownify_spider'

    start_urls = ['http://github.com/matthewwithanm/python-markdownify']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'markdownify'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
