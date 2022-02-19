import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class BLACK_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'black_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/black/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)