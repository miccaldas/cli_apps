import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest


class Jeepney_scrapy_spider(scrapy.Spider):
    name = 'jeepney_scrapy_spider'
    start_urls = ['https://pypi.org/project/jeepney/']

    @snoop
    def parse(self, response):
        srch_descriptions = response.xpath('//*[@id="description"]/div/p/text()').getall()
        for item in srch_descriptions:
            results = {'description': item}
            yield results