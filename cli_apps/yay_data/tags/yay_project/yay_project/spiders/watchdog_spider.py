import scrapy
#import snoop


class WATCHDOG_SPIDER(scrapy.Spider):
    name = 'watchdog_spider'

    start_urls = ['https://dictionary.cambridge.org/dictionary/english/watchdog']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'watchdog'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
