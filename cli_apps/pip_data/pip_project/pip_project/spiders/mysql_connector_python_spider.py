import scrapy
#import snoop


class MYSQL_CONNECTOR_PYTHON_SPIDER(scrapy.Spider):
    name = 'mysql_connector_python_spider'

    start_urls = ['http://dev.mysql.com/doc/connector-python/en/index.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'mysql-connector-python'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
