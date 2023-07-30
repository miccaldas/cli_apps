import scrapy
#import snoop


class UCLAMPSET_SPIDER(scrapy.Spider):
    name = 'uclampset_spider'

    start_urls = ['https://man7.org/linux/man-pages/man1/uclampset.1.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'uclampset'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
