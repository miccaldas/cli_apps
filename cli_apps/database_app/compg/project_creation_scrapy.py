"""
Creates the *Compg's Scrapy* project folder.
"""
import os
import pickle
import subprocess

# import snoop
from mysql.connector import Error, connect
from ScrapeSearchEngine.ScrapeSearchEngine import Startpage

# from snoop import pp

compg = os.getcwd()
project = f"{compg}/compg_project"


# @snoop
def project_creation():
    """
    Project Creation for *Arch* packages.
    Runs *Scrapy's* command to start a project::

        scrapy startproject pip_project
    """
    cmd = "/usr/bin/scrapy startproject yay_project"
    subprocess.run(cmd, cwd=compg, shell=True)


# @snoop
def settings_definition():
    """
    Settings definition for *Arch* packages.
    Defines the following options:\n
    1. FEEDS  Dictionary which structures the file that'll house the spider's results.\n
    2. RETRY_TIMES   Number of retries when there's a connection error.\n
    """
    with open(f"{project}yay_project/settings.py", "a") as d:
        d.write("FEEDS = {'results.csv': {'format': 'json', 'fields': ['name', 'content'],},}\n")
        d.write("RETRY_TIMES = 1\n")


# @snoop
def spider():
    """
    Spider creation for pip packages.
    For each entry in our packages list is built a spider, with its own file.\n
    :var str srch_title: Css query for *<h1>* elements.\n
    :var str enphasys: Css query for <em> tags. Usually sub-titles.\n
    :var str srch_text: Css query for all *<p>* tags.\n
    :var str name: The name of the package. Added so we can identify the lines in the csv.
    """
    with open(f"{compg}/names.bin", "rb") as f:
        newurls = pickle.load(f)
    for entry in newurls:
        spider_name = f"{entry[0].strip()}_spider"
        class_name = f"{spider_name}".upper()
        with open(
            f"{spiders}{spider_name}.py",
            "w",
        ) as f:
            f.write("import scrapy\n")
            f.write("#import snoop\n")
            f.write("\n\n")
            f.write(f"class {class_name}(scrapy.Spider):\n")
            f.write(f"    name = '{spider_name}'\n")
            f.write("\n")
            f.write(f"    start_urls = ['{entry[3].strip()}']")
            f.write("\n\n")
            f.write("    #@snoop\n")
            f.write("    def parse(self, response):\n")
            f.write("        srch_title = response.css('h1::text').getall()\n")
            f.write("        srch_enphasys = response.css('em::text').getall()\n")
            f.write("        srch_text = response.css('p::text').getall()\n\n")
            f.write(f"        name = '{entry[1].strip()}'\n")
            f.write("        lsts = srch_title + srch_enphasys + srch_text\n")
            f.write("        results = {'name': name, 'content': lsts}\n")
            f.write("        yield results\n")


# @snoop
def init_project():
    """
    Starts all the functions in this module.
    """
    project_creation()
    settings_definition()
    spider()


if __name__ == "__main__":
    init_project()
