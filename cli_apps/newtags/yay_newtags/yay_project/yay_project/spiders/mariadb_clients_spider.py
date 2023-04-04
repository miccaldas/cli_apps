import scrapy
#import snoop


class MARIADB_CLIENTS_SPIDER(scrapy.Spider):
    name = 'mariadb_clients_spider'

    start_urls = ['https://mariadb.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mariadb-clients'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
