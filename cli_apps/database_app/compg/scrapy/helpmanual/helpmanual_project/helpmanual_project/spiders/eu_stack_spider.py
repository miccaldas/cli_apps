import scrapy
#import snoop


class EU_STACK_SPIDER(scrapy.Spider):
    name = 'eu_stack_spider'

    start_urls = ['https://helpmanual.io/help/eu-stack/']

    #@snoop
    def parse(self, response):
        srch_nostruct = response.xpath("//*[@id='dynamic']/div[2]/main/section/div/div[1]/div[3]/div/text()").getall()
        srch_struct1 = response.xpath("//*[@id='man-page']/div/div[1]/text()").getall()
        srch_struct2 = response.xpath("//*[@id='dynamic']/div[2]/main/section/div/div[1]/div[2]/div/text()").getall()

        name = 'eu-stack'

        lsts = srch_nostruct + srch_struct1 + srch_struct2
        results = {'name': name, 'content': lsts}
        yield results
