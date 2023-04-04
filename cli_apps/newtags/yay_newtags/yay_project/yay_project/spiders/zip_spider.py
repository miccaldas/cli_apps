import scrapy
#import snoop


class ZIP_SPIDER(scrapy.Spider):
    name = 'zip_spider'

    start_urls = ['http://www.info-zip.org/Zip.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'zip'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
