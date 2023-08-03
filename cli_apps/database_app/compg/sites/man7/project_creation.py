"""
Creates the *Compg's Scrapy* project folder.
"""
import os
import pickle
import subprocess

import snoop
from dotenv import load_dotenv
from mysql.connector import Error, connect
from ScrapeSearchEngine.ScrapeSearchEngine import Startpage

# from snoop import pp
load_dotenv()

# Envs
mn7 = os.getenv("MN7")
project = os.getenv("MN7PROJ")
spiders = os.getenv("MN7SPIDERS")


# @snoop
def project_creation():
    """
    Project Creation for *Arch* packages.
    Runs *Scrapy's* command to start a project::

        scrapy startproject gnu_ftp_project
    """
    cmmd = "/usr/bin/scrapy startproject man7_project"
    subprocess.run(cmmd, cwd=mn7, shell=True)


# @snoop
def settings_definition():
    """
    Settings definition for *Arch* packages.
    Defines the following options:\n
    1. FEEDS  Dictionary which structures the file that'll house the spider's results.\n
    2. RETRY_TIMES   Number of retries when there's a connection error.\n
    """
    with open(f"{project}man7_project/settings.py", "a") as d:
        d.write("FEEDS = {'results.bin': {'format': 'pickle', 'fields': ['name', 'content'],},}\n")
        d.write("RETRY_TIMES = 1\n")

    # The 'die.net' manpage site doesn't  allow scrapers. We have to change this to use it.
    # with open(f"{project}linux_die_project/settings.py", "r") as e:
    #     lines = e.readlines()
    #     lines[19] = "ROBOTSTXT_OBEY = False"
    # with open(f"{project}linux_die_project/settings.py", "w") as m:
    #     m.writelines(lines)


@snoop
def spider():
    """
    Spider creation for compg packages.
    For each entry in our packages list is built a spider, with its own file.\n
    :var str srch_title: Css query for *<h1>* elements.\n
    :var str enphasys: Css query for <em> tags. Usually sub-titles.\n
    :var str srch_text: Css query for all *<p>* tags.\n
    :var str name: The name of the package. Added so we can identify the lines in the json.
    """

    with open(f"{mn7}spiders.bin", "rb") as f:
        newurls = pickle.load(f)
    for entry in newurls:
        spider_name = f"{entry[1]}"
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
            f.write(f"    start_urls = ['{entry[2]}']")
            f.write("\n\n")
            f.write("    #@snoop\n")
            f.write("    def parse(self, response):\n")
            f.write("        srch_gen = response.xpath(\"//*[@id='man-page']/div/div[1]/text()\").getall()\n")
            f.write("        srch_desc = response.xpath(\"//*[@id='man-page']/div/div[1]/text()[1]\").getall()\n")
            # DON'T ALIGN THIS LINE! It's like that because it has the 'f' for
            # f-expression before it. Leave it be.
            f.write(f"        name = '{entry[0]}'\n\n")
            f.write("        lsts = srch_desc + srch_gen\n")
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
