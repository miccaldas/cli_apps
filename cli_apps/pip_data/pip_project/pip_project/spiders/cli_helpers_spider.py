import scrapy
#import snoop


class CLI_HELPERS_SPIDER(scrapy.Spider):
    name = 'cli_helpers_spider'

    start_urls = ['https://github.com/dbcli/cli_helpers']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cli-helpers'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
