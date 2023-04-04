import scrapy
#import snoop


class LESSPIPE_SPIDER(scrapy.Spider):
    name = 'lesspipe_spider'

    start_urls = ['https://www-zeuthen.desy.de/~friebel/unix/lesspipe.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'lesspipe'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
