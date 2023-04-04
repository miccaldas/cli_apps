import scrapy
#import snoop


class OPENSSH_SPIDER(scrapy.Spider):
    name = 'openssh_spider'

    start_urls = ['https://www.openssh.com/portable.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'openssh'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
