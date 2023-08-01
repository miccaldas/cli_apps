"""
Creates the *Compg's Scrapy* project folder.
"""
import os
import pickle
import subprocess

from dotenv import load_dotenv

# import snoop
from mysql.connector import Error, connect
from ScrapeSearchEngine.ScrapeSearchEngine import Startpage

# from snoop import pp
load_dotenv()

# Envs
cmd = os.getenv("CMD")
project = os.getenv("CMDPROJ")
spiders = os.getenv("CMDSPIDERS")


# @snoop
def project_creation():
    """
    Project Creation for *Arch* packages.
    Runs *Scrapy's* command to start a project::

        scrapy startproject github_project
    """
    cmmd = "/usr/bin/scrapy startproject command_linux_project"
    subprocess.run(cmmd, cwd=cmd, shell=True)


# @snoop
def settings_definition():
    """
    Settings definition for *Arch* packages.
    Defines the following options:\n
    1. FEEDS  Dictionary which structures the file that'll house the spider's results.\n
    2. RETRY_TIMES   Number of retries when there's a connection error.\n
    """
    with open(f"{project}command_linux_project/settings.py", "a") as d:
        d.write("FEEDS = {'results.bin': {'format': 'pickle', 'fields': ['name', 'content'],},}\n")
        d.write("RETRY_TIMES = 1\n")


# @snoop
def spider():
    """
    Spider creation for compg packages.
    For each entry in our packages list is built a spider, with its own file.\n
    :var str srch_title: Css query for *<h1>* elements.\n
    :var str enphasys: Css query for <em> tags. Usually sub-titles.\n
    :var str srch_text: Css query for all *<p>* tags.\n
    :var str name: The name of the package. Added so we can identify the lines in the json.
    """

    with open(f"{cmd}spiders.bin", "rb") as f:
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
            f.write("        srch_text = response.xpath('/html/body').get()\n\n")
            f.write("        des = srch_text.split('DESCRIPTION')[1]\n")
            f.write("        desc = des.split('EXIT')[0]\n")
            f.write("        notitle = desc.replace('<h2>', '').replace('</h2>', '')\n")
            f.write("        noitalics = notitle.replace('<i>', '').replace('</i>', '')\n")
            f.write("        nobrks = noitalics.replace('\\n', ' ')\n")
            f.write("        nobold = nobrks.replace('<b>', '').replace('</b>', '')\n")
            f.write("        notxt = nobold.replace('<p>', '').replace('</p>', '')\n")
            f.write("        txt = notxt.split('<a')[0]\n")
            # DON'T ALIGN THIS LINE! It's like that because it has the 'f' for
            # f-expression before it. Leave it be.
            f.write(f"        name = '{entry[0]}'\n\n")
            f.write("        lsts = txt\n")
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
