import scrapy
#import snoop


class JAVA_RUNTIME_COMMON_SPIDER(scrapy.Spider):
    name = 'java_runtime_common_spider'

    start_urls = ['https://www.archlinux.org/packages/extra/any/java-common/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'java-runtime-common'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results