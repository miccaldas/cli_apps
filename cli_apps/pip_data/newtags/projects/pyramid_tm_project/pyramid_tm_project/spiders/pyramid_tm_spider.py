import scrapy   # noqa: F401
import snoop


class PYRAMID_TM_SPIDER(scrapy.Spider):
    name = 'pyramid_tm_spider'

    start_urls = ["https://github.com/Pylons/pyramid_tm"]

    @snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()
        srch_lists = response.css('li::text').getall()

        lsts = srch_title + srch_enphasys, srch_text + srch_lists
        results = {"content": lsts}

        yield results
        