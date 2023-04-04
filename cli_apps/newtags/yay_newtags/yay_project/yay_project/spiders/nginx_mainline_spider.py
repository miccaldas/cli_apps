import scrapy
#import snoop


class NGINX_MAINLINE_SPIDER(scrapy.Spider):
    name = 'nginx_mainline_spider'

    start_urls = ['https://nginx.org']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'nginx-mainline'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
