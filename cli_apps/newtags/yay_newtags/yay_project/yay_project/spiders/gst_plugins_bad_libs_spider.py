import scrapy
#import snoop


class GST_PLUGINS_BAD_LIBS_SPIDER(scrapy.Spider):
    name = 'gst_plugins_bad_libs_spider'

    start_urls = ['https://gstreamer.freedesktop.org/']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'gst-plugins-bad-libs'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
