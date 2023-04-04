import scrapy
#import snoop


class PYTHON_BACKPORTS_CSV_SPIDER(scrapy.Spider):
    name = 'python_backports_csv_spider'

    start_urls = ['https://github.com/ryanhiebert/backports.csv']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-backports.csv'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
