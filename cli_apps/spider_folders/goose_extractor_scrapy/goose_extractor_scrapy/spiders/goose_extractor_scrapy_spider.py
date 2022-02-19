import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class GOOSE_EXTRACTOR_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'goose_extractor_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/goose-extractor/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)