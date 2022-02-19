import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class NEWSPAPER3K_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'newspaper3k_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/newspaper3k/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)