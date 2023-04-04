import scrapy
#import snoop


class MAN_DB_SPIDER(scrapy.Spider):
    name = 'man_db_spider'

    start_urls = ['https://gitlab.com/cjwatson/man-db']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'man-db'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
