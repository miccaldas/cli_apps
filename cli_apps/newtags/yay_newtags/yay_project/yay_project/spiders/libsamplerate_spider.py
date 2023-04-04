import scrapy
#import snoop


class LIBSAMPLERATE_SPIDER(scrapy.Spider):
    name = 'libsamplerate_spider'

    start_urls = ['https://libsndfile.github.io/libsamplerate/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsamplerate'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
