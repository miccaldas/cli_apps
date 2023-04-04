import scrapy
#import snoop


class LIBSNDFILE_SPIDER(scrapy.Spider):
    name = 'libsndfile_spider'

    start_urls = ['https://libsndfile.github.io/libsndfile/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libsndfile'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
