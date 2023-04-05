import scrapy
#import snoop


class NVIDIA_CUBLAS_CU11_SPIDER(scrapy.Spider):
    name = 'nvidia_cublas_cu11_spider'

    start_urls = ['https://developer.nvidia.com/cuda-zone']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nvidia-cublas-cu11'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
