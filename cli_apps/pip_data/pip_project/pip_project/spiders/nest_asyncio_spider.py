import scrapy
#import snoop


class NEST_ASYNCIO_SPIDER(scrapy.Spider):
    name = 'nest_asyncio_spider'

    start_urls = ['https://github.com/erdewit/nest_asyncio']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nest-asyncio'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
