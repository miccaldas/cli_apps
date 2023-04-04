import scrapy
#import snoop


class JAVA_SERVICE_WRAPPER_SPIDER(scrapy.Spider):
    name = 'java_service_wrapper_spider'

    start_urls = ['https://wrapper.tanukisoftware.com/doc/english/introduction.html']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'java-service-wrapper'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
