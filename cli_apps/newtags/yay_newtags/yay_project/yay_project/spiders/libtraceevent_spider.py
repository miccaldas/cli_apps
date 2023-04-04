import scrapy
#import snoop


class LIBTRACEEVENT_SPIDER(scrapy.Spider):
    name = 'libtraceevent_spider'

    start_urls = ['https://git.kernel.org/pub/scm/libs/libtrace/libtraceevent.git/about/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'libtraceevent'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
