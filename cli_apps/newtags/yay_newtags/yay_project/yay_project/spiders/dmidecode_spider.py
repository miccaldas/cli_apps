import scrapy
#import snoop


class DMIDECODE_SPIDER(scrapy.Spider):
    name = 'dmidecode_spider'

    start_urls = ['https://www.nongnu.org/dmidecode']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dmidecode'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
