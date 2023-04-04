import scrapy
#import snoop


class LIBNFTNL_SPIDER(scrapy.Spider):
    name = 'libnftnl_spider'

    start_urls = ['https://netfilter.org/projects/libnftnl/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libnftnl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
