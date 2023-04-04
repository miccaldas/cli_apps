import scrapy
#import snoop


class TRASH_CLI_SPIDER(scrapy.Spider):
    name = 'trash_cli_spider'

    start_urls = ['https://github.com/andreafrancia/trash-cli']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'trash-cli'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
