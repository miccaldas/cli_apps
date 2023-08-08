import scrapy
#import snoop


class JRE_OPENJDK_SPIDER(scrapy.Spider):
    name = 'jre_openjdk_spider'

    start_urls = ['https://openjdk.java.net/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'jre-openjdk'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
