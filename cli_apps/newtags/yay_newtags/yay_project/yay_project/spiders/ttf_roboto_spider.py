import scrapy
#import snoop


class TTF_ROBOTO_SPIDER(scrapy.Spider):
    name = 'ttf_roboto_spider'

    start_urls = ['https://material.google.com/style/typography.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ttf-roboto'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
