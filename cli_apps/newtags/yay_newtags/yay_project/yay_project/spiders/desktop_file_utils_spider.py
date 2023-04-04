import scrapy
#import snoop


class DESKTOP_FILE_UTILS_SPIDER(scrapy.Spider):
    name = 'desktop_file_utils_spider'

    start_urls = ['https://www.freedesktop.org/wiki/Software/desktop-file-utils']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'desktop-file-utils'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
