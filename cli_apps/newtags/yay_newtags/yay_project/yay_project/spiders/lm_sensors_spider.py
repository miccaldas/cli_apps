import scrapy
#import snoop


class LM_SENSORS_SPIDER(scrapy.Spider):
    name = 'lm_sensors_spider'

    start_urls = ['https://hwmon.wiki.kernel.org/lm_sensors']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'lm_sensors'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
