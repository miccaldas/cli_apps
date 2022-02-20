import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest


class Ipython_genutils_scrapy_spider(scrapy.Spider):
    name = 'ipython_genutils_scrapy_spider'
    start_urls = ['https://pypi.org/project/ipython_genutils/']

    @snoop
    def parse(self, response):
        srch_descriptions = response.xpath('//*[@id="description"]/div/p/text()').getall()
        for item in srch_descriptions:
            results = {'description': item}
            yield results