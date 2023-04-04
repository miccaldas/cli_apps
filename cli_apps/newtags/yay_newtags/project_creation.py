"""
Creates the *Scrapy* project folder.
"""
import os
import pickle
import subprocess

import snoop
from snoop import pp


@snoop
def project_creation():
    """
    Runs *Scrapy's* command to start a project.\n
    :var str cmd: *scrapy startproject yay_project*.
    """
    cwd = os.getcwd()
    cmd = "scrapy startproject yay_project"
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    project_creation()


@snoop
def settings_definition():
    """
    Defines the following options:\n
    1. FEED_EXPORT_FIELDS.  Title of the csv columns.
    2.  FEED_FORMAT. *csv*.
    3. FEED_URI.  *results.csv*
    4. RETRY_TIMES   Number of retries when there's a connection error.\n
    .. NOTE:: The feeds definitions will be deprecated in the near future.
    """

    with open("yay_project/yay_project/settings.py", "a") as d:
        d.write("ITEM_PIPELINES = {'scrapy.pipelines.images.ImagesPipeline': 1}")
        d.write("\n")
        d.write('FEED_EXPORT_FIELDS = ["name", "content"]')
        d.write("\n")
        d.write('FEED_FORMAT = "csv"')
        d.write("\n")
        d.write('FEED_URI = "results.csv"')
        d.write("\n")
        d.write("RETRY_TIMES = 1\n")
        d.close()
    with open("yay_project/yay_project/pipelines.py", "r") as f:
        lines = f.readlines()
    with open("yay_project/yay_project/pipelines.py", "w") as f:
        for line in lines:
            f.write(line)
        f.write("\n")
        f.write("        return item")


if __name__ == "__main__":
    settings_definition()


@snoop
def spider():
    """
    For each entry in our packages list is built a spider, that'llhave its own file.\n
    :var str srch_title: Css query for *<h1>* elements.\n
    :var str enphasys: Css query for <em> tags. Usually sub-titles.\n
    :var str srch_text: Css query for all *<p>* tags.\n
    :var str name: The name of the package. Added so we can identify the lines in the csv.
    """

    with open("newurls.bin", "rb") as f:
        newurls = pickle.load(f)

    for entry in newurls:
        spider_name = f"{entry[0]}_spider"
        class_name = f"{spider_name}".upper()
        with open(
            f"yay_project/yay_project/spiders/{spider_name}.py",
            "w",
        ) as f:
            f.write("import scrapy\n")
            f.write("#import snoop\n")
            f.write("\n\n")
            f.write(f"class {class_name}(scrapy.Spider):\n")
            f.write(f"    name = '{spider_name}'\n")
            f.write("\n")
            f.write(f"    start_urls = ['{entry[2]}']")
            f.write("\n\n")
            f.write("    #@snoop\n")
            f.write("    def parse(self, response):\n")
            f.write("        srch_title = response.css('h1::text').getall()\n")
            f.write("        srch_enphasys = response.css('em::text').getall()\n")
            f.write("        srch_text = response.css('p::text').getall()\n\n")
            f.write(f"        name = '{entry[1]}'\n")
            f.write("        lsts = srch_title + srch_enphasys + srch_text\n")
            f.write("        results = {'name': name, 'content': lsts}\n")
            f.write("        yield results\n")


if __name__ == "__main__":
    spider()
