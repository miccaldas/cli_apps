import scrapy
#import snoop


class SHARED_MIME_INFO_SPIDER(scrapy.Spider):
    name = 'shared_mime_info_spider'

    start_urls = ['https://www.freedesktop.org/wiki/Specifications/shared-mime-info-spec/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'shared-mime-info'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
