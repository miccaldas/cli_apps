import scrapy
#import snoop


class CABEXTRACT_SPIDER(scrapy.Spider):
    name = 'cabextract_spider'

    start_urls = ['https://www.cabextract.org.uk/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'cabextract'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results