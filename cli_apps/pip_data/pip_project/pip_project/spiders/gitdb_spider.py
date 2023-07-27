import scrapy
#import snoop


class GITDB_SPIDER(scrapy.Spider):
    name = 'gitdb_spider'

    start_urls = ['https://github.com/gitpython-developers/gitdb']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gitdb'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
