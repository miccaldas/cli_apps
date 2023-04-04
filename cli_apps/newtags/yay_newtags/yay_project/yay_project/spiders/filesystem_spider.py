import scrapy
#import snoop


class FILESYSTEM_SPIDER(scrapy.Spider):
    name = 'filesystem_spider'

    start_urls = ['https://archlinux.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'filesystem'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results