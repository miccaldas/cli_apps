import scrapy
#import snoop


class ENCFS_SPIDER(scrapy.Spider):
    name = 'encfs_spider'

    start_urls = ['https://vgough.github.io/encfs/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'encfs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
