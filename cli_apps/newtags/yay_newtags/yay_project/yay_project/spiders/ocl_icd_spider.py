import scrapy
#import snoop


class OCL_ICD_SPIDER(scrapy.Spider):
    name = 'ocl_icd_spider'

    start_urls = ['https://github.com/OCL-dev/ocl-icd']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'ocl-icd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
