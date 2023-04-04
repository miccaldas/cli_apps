import scrapy
#import snoop


class PROCPS_NG_SPIDER(scrapy.Spider):
    name = 'procps_ng_spider'

    start_urls = ['https://gitlab.com/procps-ng/procps']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'procps-ng'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
