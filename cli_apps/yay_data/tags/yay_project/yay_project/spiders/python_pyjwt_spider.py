import scrapy
#import snoop


class PYTHON_PYJWT_SPIDER(scrapy.Spider):
    name = 'python_pyjwt_spider'

    start_urls = ['https://github.com/jpadilla/pyjwt']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-pyjwt'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
