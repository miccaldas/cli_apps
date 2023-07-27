import scrapy
#import snoop


class CLICK_PLUGINS_SPIDER(scrapy.Spider):
    name = 'click_plugins_spider'

    start_urls = ['https://github.com/click-contrib/click-plugins']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'click-plugins'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
