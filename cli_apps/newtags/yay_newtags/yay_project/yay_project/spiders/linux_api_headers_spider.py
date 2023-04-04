import scrapy
#import snoop


class LINUX_API_HEADERS_SPIDER(scrapy.Spider):
    name = 'linux_api_headers_spider'

    start_urls = ['https://www.gnu.org/software/libc']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'linux-api-headers'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
