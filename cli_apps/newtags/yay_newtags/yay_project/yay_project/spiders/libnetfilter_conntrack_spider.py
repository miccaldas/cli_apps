import scrapy
#import snoop


class LIBNETFILTER_CONNTRACK_SPIDER(scrapy.Spider):
    name = 'libnetfilter_conntrack_spider'

    start_urls = ['https://www.netfilter.org/projects/libnetfilter_conntrack/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libnetfilter_conntrack'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
