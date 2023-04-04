import scrapy
#import snoop


class PYTHON_MYSQL_CONNECTOR_SPIDER(scrapy.Spider):
    name = 'python_mysql_connector_spider'

    start_urls = ['https://dev.mysql.com/downloads/connector/python/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-mysql-connector'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
