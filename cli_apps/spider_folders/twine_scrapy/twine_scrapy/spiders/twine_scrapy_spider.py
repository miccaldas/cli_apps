import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class TWINE_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'twine_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/twine/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)