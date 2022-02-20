import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest


class Tzlocal_scrapy_spider(scrapy.Spider):
    name = 'tzlocal_scrapy_spider'
    start_urls = ['https://pypi.org/project/tzlocal/']

    @snoop
    def parse(self, response):
        srch_descriptions = response.xpath('//*[@id="description"]/div/p/text()').getall()
        for item in srch_descriptions:
            results = {'description': item}
            yield results