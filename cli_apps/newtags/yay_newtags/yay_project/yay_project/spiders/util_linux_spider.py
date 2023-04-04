import scrapy
#import snoop


class UTIL_LINUX_SPIDER(scrapy.Spider):
    name = 'util_linux_spider'

    start_urls = ['https://github.com/karelzak/util-linux']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'util-linux'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
