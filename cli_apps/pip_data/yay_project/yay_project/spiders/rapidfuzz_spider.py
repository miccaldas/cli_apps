import scrapy
#import snoop


class RAPIDFUZZ_SPIDER(scrapy.Spider):
    name = 'rapidfuzz_spider'

    start_urls = ['https://github.com/maxbachmann/RapidFuzz']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'rapidfuzz'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
