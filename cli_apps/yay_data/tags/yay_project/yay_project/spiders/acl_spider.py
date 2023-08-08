import scrapy
#import snoop


class ACL_SPIDER(scrapy.Spider):
    name = 'acl_spider'

    start_urls = ['https://savannah.nongnu.org/projects/acl']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'acl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
