import scrapy
#import snoop


class MOVIEPY_SPIDER(scrapy.Spider):
    name = 'moviepy_spider'

    start_urls = ['https://zulko.github.io/moviepy/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'moviepy'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
