import scrapy
#import snoop


class MD4C_SPIDER(scrapy.Spider):
    name = 'md4c_spider'

    start_urls = ['https://github.com/mity/md4c']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'md4c'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
