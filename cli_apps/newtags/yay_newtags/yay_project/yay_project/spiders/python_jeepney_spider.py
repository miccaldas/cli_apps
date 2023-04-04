import scrapy
#import snoop


class PYTHON_JEEPNEY_SPIDER(scrapy.Spider):
    name = 'python_jeepney_spider'

    start_urls = ['https://gitlab.com/takluyver/jeepney']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-jeepney'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
