import scrapy
#import snoop


class PAMDEINTERLACE_SPIDER(scrapy.Spider):
    name = 'pamdeinterlace_spider'

    start_urls = ['https://linux.die.net/man/1/pamdeinterlace']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'pamdeinterlace'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
