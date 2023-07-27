import scrapy
#import snoop


class LINE_PROFILER_SPIDER(scrapy.Spider):
    name = 'line_profiler_spider'

    start_urls = ['https://github.com/pyutils/line_profiler']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'line-profiler'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
