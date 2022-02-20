import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest


class Outcome_scrapy_spider(scrapy.Spider):
    name = 'outcome_scrapy_spider'
    start_urls = ['https://pypi.org/project/outcome/']

    @snoop
    def parse(self, response):
        srch_descriptions = response.xpath('//*[@id="description"]/div/p/text()').getall()
        for item in srch_descriptions:
            results = {'description': item}
            yield results