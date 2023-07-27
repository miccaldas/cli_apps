import scrapy
#import snoop


class OPENCV_PYTHON_SPIDER(scrapy.Spider):
    name = 'opencv_python_spider'

    start_urls = ['https://github.com/opencv/opencv-python']

    #@snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()

        name = 'opencv-python'
        lsts = srch_title + srch_enphasys + srch_text
        results = {'name': name, 'content': lsts}
        yield results
