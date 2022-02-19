import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class TRIO_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'trio_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/trio/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)