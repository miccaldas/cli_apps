import scrapy
#import snoop


class XDOTOOL_SPIDER(scrapy.Spider):
    name = 'xdotool_spider'

    start_urls = ['https://www.semicomplete.com/projects/xdotool/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'xdotool'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
