import scrapy
#import snoop


class EN_CORE_WEB_SM_SPIDER(scrapy.Spider):
    name = 'en_core_web_sm_spider'

    start_urls = ['https://explosion.ai']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'en-core-web-sm'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
