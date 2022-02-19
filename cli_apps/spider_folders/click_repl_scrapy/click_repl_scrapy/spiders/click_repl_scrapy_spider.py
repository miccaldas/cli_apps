import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class CLICK_REPL_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'click_repl_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/click-repl/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)