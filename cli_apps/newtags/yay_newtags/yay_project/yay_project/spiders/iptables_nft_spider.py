import scrapy
#import snoop


class IPTABLES_NFT_SPIDER(scrapy.Spider):
    name = 'iptables_nft_spider'

    start_urls = ['https://www.netfilter.org/projects/iptables/index.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'iptables-nft'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
