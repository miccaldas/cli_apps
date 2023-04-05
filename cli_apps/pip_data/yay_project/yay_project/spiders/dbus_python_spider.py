import scrapy
#import snoop


class DBUS_PYTHON_SPIDER(scrapy.Spider):
    name = 'dbus_python_spider'

    start_urls = ['http://www.freedesktop.org/wiki/Software/DBusBindings/#python']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'dbus-python'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
