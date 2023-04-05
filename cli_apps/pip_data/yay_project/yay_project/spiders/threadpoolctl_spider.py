import scrapy
#import snoop


class THREADPOOLCTL_SPIDER(scrapy.Spider):
    name = 'threadpoolctl_spider'

    start_urls = ['https://github.com/joblib/threadpoolctl']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'threadpoolctl'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
