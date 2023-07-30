import scrapy
#import snoop


class BD_INFO_SPIDER(scrapy.Spider):
    name = 'bd_info_spider'

    start_urls = ['https://manpages.debian.org/testing/libbluray-bin/bd_info.1.en.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'bd_info'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
