"""
Automates the creation of Scrapy projects.
This file was ran from inside the 'projects' folder,
where all the 'scrapy' folders were. For some reason,
Python doesn't consider 'cli_apps' a package.
"""

import subprocess

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


class ScrapyProject:
    """In this class will be represented the steps needed to setup
    a Scrapy project. Each method will be a task."""

    def __init__(self, project_name, spider_name, domain):
        self.project_name = project_name
        self.spider_name = spider_name
        self.domain = domain

    # @snoop
    def project_creation(self):
        """Where will create a scrapy project in location and
        name to be defined."""

        cmd = f"scrapy startproject {self.project_name}"
        subprocess.run(cmd, shell=True)

    # @snoop
    def settings_definition(self):
        """We'll deal with all the usual changes on
        the settings."""

        with open(f"{self.project_name}/{self.project_name}/settings.py", "a") as d:
            d.write("ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}")
            d.write("\n")
            d.write('FEED_EXPORT_FIELDS = ["content"]')
            d.write("\n")
            d.write('FEED_FORMAT = "csv"')
            d.write("\n")
            d.write('FEED_URI = "results.csv"')
            d.write("\n")
            d.close()
        with open(f"{self.project_name}/{self.project_name}/pipelines.py", "r") as f:
            lines = f.readlines()
            # lines = lines[:-1]
        with open(f"{self.project_name}/{self.project_name}/pipelines.py", "w") as f:
            for line in lines:
                f.write(line)
            f.write("\n")
            f.write("        return item")

    # @snoop
    def spider(self):
        """We recreate the spider definition folder."""

        class_name = f"{self.spider_name}".upper()
        with open(
            f"{self.project_name}/{self.project_name}/spiders/{self.spider_name}.py",
            "w",
        ) as f:
            f.write("import scrapy   # noqa: F401\n")
            f.write("import snoop\n")
            f.write("\n\n")
            f.write(f"class {class_name}(scrapy.Spider):\n")
            f.write(f"    name = '{self.spider_name}'\n")
            f.write("\n")
            f.write(f'    start_urls = ["{self.domain}"]')
            f.write("\n")
            f.write(
                """
    @snoop
    def parse(self, response):
        srch_title = response.css('h1::text').getall()
        srch_enphasys = response.css('em::text').getall()
        srch_text = response.css('p::text').getall()
        srch_lists = response.css('li::text').getall()

        lsts = srch_title + srch_enphasys, srch_text + srch_lists
        results = {"content": lsts}

        yield results
        """
            )


if __name__ == "__main__":
    (ScrapyProject)
