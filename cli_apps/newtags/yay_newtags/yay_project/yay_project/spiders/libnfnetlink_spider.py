import scrapy
#import snoop


class LIBNFNETLINK_SPIDER(scrapy.Spider):
    name = 'libnfnetlink_spider'

    start_urls = ['https://www.netfilter.org/projects/libnfnetlink/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libnfnetlink'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
