import scrapy
#import snoop


class MYSQLCLIENT_SPIDER(scrapy.Spider):
    name = 'mysqlclient_spider'

    start_urls = ['https://github.com/PyMySQL/mysqlclient']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mysqlclient'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
