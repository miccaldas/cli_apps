import scrapy
#import snoop


class SYSTEMD_SPIDER(scrapy.Spider):
    name = 'systemd_spider'

    start_urls = ['https://www.github.com/systemd/systemd']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'systemd'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
