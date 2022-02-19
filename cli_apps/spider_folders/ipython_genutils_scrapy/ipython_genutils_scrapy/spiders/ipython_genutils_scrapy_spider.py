import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class IPYTHON_GENUTILS_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'ipython_genutils_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/ipython_genutils/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)