import scrapy
#import snoop


class ENGLISH_WORDS_SPIDER(scrapy.Spider):
    name = 'english_words_spider'

    start_urls = ['https://github.com/mwiens91/english-words-py']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'english-words'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
