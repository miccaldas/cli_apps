import scrapy
#import snoop


class NFTABLES_SPIDER(scrapy.Spider):
    name = 'nftables_spider'

    start_urls = ['https://netfilter.org/projects/nftables/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nftables'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results