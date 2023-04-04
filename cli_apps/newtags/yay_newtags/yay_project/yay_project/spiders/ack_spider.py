import scrapy
import snoop


class ACK_SPIDER(scrapy.Spider):
    name = "ack_spider"

    start_urls = ["http://betterthangrep.com/"]

    @snoop
    def parse(self, response):
        srch_title = response.css("h1::text").getall()
        srch_enphasys = response.css("em::text").getall()
        srch_text = response.css("p::text").getall()

        name = "ack"
        lsts = srch_title + srch_enphasys + srch_text
        results = {"name": name, "content": lsts}
        yield results
