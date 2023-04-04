import scrapy
#import snoop


class GITHUB_CLI_SPIDER(scrapy.Spider):
    name = 'github_cli_spider'

    start_urls = ['https://github.com/cli/cli']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'github-cli'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
