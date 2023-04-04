import scrapy
#import snoop


class LIBIXION_SPIDER(scrapy.Spider):
    name = 'libixion_spider'

    start_urls = ['https://gitlab.com/ixion/ixion/blob/master/README.md']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libixion'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
