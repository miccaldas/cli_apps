import scrapy
#import snoop


class PLAYSOUND_SPIDER(scrapy.Spider):
    name = 'playsound_spider'

    start_urls = ['https://github.com/TaylorSMarks/playsound']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'playsound'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
