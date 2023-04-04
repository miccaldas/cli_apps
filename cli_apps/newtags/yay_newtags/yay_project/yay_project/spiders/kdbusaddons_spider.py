import scrapy
#import snoop


class KDBUSADDONS_SPIDER(scrapy.Spider):
    name = 'kdbusaddons_spider'

    start_urls = ['https://community.kde.org/Frameworks']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'kdbusaddons'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results