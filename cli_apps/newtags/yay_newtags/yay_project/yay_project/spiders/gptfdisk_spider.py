import scrapy
#import snoop


class GPTFDISK_SPIDER(scrapy.Spider):
    name = 'gptfdisk_spider'

    start_urls = ['https://www.rodsbooks.com/gdisk/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gptfdisk'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
