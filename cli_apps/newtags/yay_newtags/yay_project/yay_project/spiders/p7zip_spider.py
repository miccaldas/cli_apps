import scrapy
#import snoop


class P7ZIP_SPIDER(scrapy.Spider):
    name = 'p7zip_spider'

    start_urls = ['https://github.com/p7zip-project/p7zip']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'p7zip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
