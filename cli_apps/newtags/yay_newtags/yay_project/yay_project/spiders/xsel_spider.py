import scrapy
#import snoop


class XSEL_SPIDER(scrapy.Spider):
    name = 'xsel_spider'

    start_urls = ['https://vergenet.net/~conrad/software/xsel/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xsel'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
