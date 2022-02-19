import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class GEVENT_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'gevent_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/gevent/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)