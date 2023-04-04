import scrapy
#import snoop


class FIREFOX_SPIDER(scrapy.Spider):
    name = 'firefox_spider'

    start_urls = ['https://www.mozilla.org/firefox/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'firefox'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
