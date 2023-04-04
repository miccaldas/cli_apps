import scrapy
#import snoop


class SIGNON_UI_SPIDER(scrapy.Spider):
    name = 'signon_ui_spider'

    start_urls = ['https://launchpad.net/online-accounts-signon-ui']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'signon-ui'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
