import scrapy
#import snoop


class PYTHON_NAUTILUS_SPIDER(scrapy.Spider):
    name = 'python_nautilus_spider'

    start_urls = ['https://wiki.gnome.org/Projects/NautilusPython']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'python-nautilus'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
