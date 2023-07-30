import scrapy
#import snoop


class GIF2WEBP_SPIDER(scrapy.Spider):
    name = 'gif2webp_spider'

    start_urls = ['https://github.com/imagemin/gif2webp-bin']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gif2webp'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
