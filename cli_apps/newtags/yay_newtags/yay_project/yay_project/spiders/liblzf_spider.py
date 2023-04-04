import scrapy
#import snoop


class LIBLZF_SPIDER(scrapy.Spider):
    name = 'liblzf_spider'

    start_urls = ['http://software.schmorp.de/pkg/liblzf.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'liblzf'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
