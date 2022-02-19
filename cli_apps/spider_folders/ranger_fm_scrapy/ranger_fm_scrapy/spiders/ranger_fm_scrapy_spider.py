import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class RANGER_FM_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'ranger_fm_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/ranger-fm/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)