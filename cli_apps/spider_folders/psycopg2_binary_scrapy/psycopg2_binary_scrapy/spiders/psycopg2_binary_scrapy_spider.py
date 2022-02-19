import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class PSYCOPG2_BINARY_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'psycopg2_binary_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/psycopg2-binary/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)