import scrapy
#import snoop


class DEFAULT_CURSORS_SPIDER(scrapy.Spider):
    name = 'default_cursors_spider'

    start_urls = ['https://archlinux.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'default-cursors'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
