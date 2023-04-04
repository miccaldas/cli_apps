import scrapy
#import snoop


class VULKAN_ICD_LOADER_SPIDER(scrapy.Spider):
    name = 'vulkan_icd_loader_spider'

    start_urls = ['https://www.khronos.org/vulkan/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'vulkan-icd-loader'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
