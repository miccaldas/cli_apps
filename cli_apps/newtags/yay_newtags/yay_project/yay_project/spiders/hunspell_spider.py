import scrapy
#import snoop


class HUNSPELL_SPIDER(scrapy.Spider):
    name = 'hunspell_spider'

    start_urls = ['https://github.com/hunspell/hunspell']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'hunspell'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
