import scrapy
#import snoop


class SIGNON_PLUGIN_OAUTH2_SPIDER(scrapy.Spider):
    name = 'signon_plugin_oauth2_spider'

    start_urls = ['https://gitlab.com/accounts-sso/signon-plugin-oauth2']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'signon-plugin-oauth2'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
