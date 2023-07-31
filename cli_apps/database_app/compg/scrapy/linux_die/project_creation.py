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
die = os.getenv("DIE")
project = os.getenv("DIEPROJ")
spiders = os.getenv("DIESPIDERS")


# @snoop
def project_creation():
    """
    Project Creation for *Arch* packages.
    Runs *Scrapy's* command to start a project::

        scrapy startproject pip_project
    """
    cmd = "/usr/bin/scrapy startproject linuxx_die_project"
    subprocess.run(cmd, cwd=die, shell=True)


# @snoop
def settings_definition():
    """
    Settings definition for *Arch* packages.
    Defines the following options:\n
    1. FEEDS  Dictionary which structures the file that'll house the spider's results.\n
    2. RETRY_TIMES   Number of retries when there's a connection error.\n
    3: ROBOTSTXT_OBEY   We won't obey *robots.txt*.
    """
    with open(f"{project}linux_die_project/settings.py", "a") as d:
        d.write("FEEDS = {'results.bin': {'format': 'pickle', 'fields': ['name', 'content'],},}\n")
        d.write("RETRY_TIMES = 1\n")

    # The 'die.net' manpage site doesn't  allow scrapers. We have to change this to use it.
    with open(f"{project}linux_die_project/settings.py", "r") as e:
        lines = e.readlines()
        lines[19] = "ROBOTSTXT_OBEY = False"

    with open(f"{project}linux_die_project/settings.py", "w") as m:
        m.writelines(lines)


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
    with open(f"{die}spiders.bin", "rb") as f:
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
            f.write("        srch_text = response.xpath('//html/body/div[1]/div[2]/p').getall()\n")
            # DON'T ALIGN THIS LINE! It's like that because it has the 'f' for
            # f-expression before it. Leave it be.
            f.write(f"        name = '{entry[0]}'\n\n")
            f.write("        ct = []\n")
            f.write("        for s in srch_text:\n")
            f.write("            ps = s.replace('<p>', '').replace('</p>', '')\n")
            f.write("            bs = ps.replace('<b>', '').replace('</b>', '')\n")
            f.write("            ct.append(bs)\n")
            f.write("        for n in ct:\n")
            f.write("            if (\n")
            f.write("               n.startswith('Copyright')\n")
            f.write("               or n.startswith('[<i>')\n")
            f.write("               or n.startswith('<a href')\n")
            f.write("            ):\n")
            f.write("               ct.remove(n)\n")
            f.write("        clean_text = [i.strip() for i in ct]\n\n")
            f.write("        lists = clean_text\n")
            f.write("        results = {'name': name, 'content': lists}\n")
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
