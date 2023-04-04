import scrapy
#import snoop


class JDK8_OPENJDK_SPIDER(scrapy.Spider):
    name = 'jdk8_openjdk_spider'

    start_urls = ['https://openjdk.java.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jdk8-openjdk'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
