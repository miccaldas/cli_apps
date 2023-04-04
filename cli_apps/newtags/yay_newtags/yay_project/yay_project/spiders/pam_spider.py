import scrapy
#import snoop


class PAM_SPIDER(scrapy.Spider):
    name = 'pam_spider'

    start_urls = ['http://linux-pam.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pam'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
