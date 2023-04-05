import scrapy
#import snoop


class SEND2TRASH_SPIDER(scrapy.Spider):
    name = 'Send2Trash_spider'

    start_urls = ['https://github.com/arsenetar/send2trash']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'Send2Trash'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
