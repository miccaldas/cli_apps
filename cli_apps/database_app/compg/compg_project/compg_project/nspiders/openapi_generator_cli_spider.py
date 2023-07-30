import scrapy
#import snoop


class OPENAPI_GENERATOR_CLI_SPIDER(scrapy.Spider):
    name = 'openapi_generator_cli_spider'

    start_urls = ['https://github.com/OpenAPITools/openapi-generator-cli']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'openapi-generator-cli'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
