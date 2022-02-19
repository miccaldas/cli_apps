import scrapy   # noqa: F401
import snoop
import isort   # noqa: F401
from itertools import zip_longest

class ET_XMLFILE_SCRAPY_SPIDER.PY(scrapy.Spider):
    name = 'et_xmlfile_scrapy_spider.py'

    start_urls = ['https://pypi.org/project/et-xmlfile/
']

    srch_descriptions = response.xpath('//h1/text()').getall()

    results = {src_descriptions}
    yield results)