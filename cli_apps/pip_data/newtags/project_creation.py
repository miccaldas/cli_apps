"""
Prepares and collects the information needed to create
Scrapy projects for each of the Pip installed packages.
These projects will be used in collecting keywords from
the documentation/github sites of each package.
This page was ran from the 'projects' folder, because
Python doesn't accept 'cli_apps' as a package.
"""
import os

from newtags_scrapy_class import ScrapyProject

# import snoop
# from snoop import pp


# @snoop
def project_creation():
    """
    'urls2' is a folder with files for each installed Pip package,
    named accordingly, containing the url for github or their docs
    site. Using a list of its files, we clean their titles from
    punctuation marks and dashes, that Scrapy doesn't accept in their
    projects/spider's names, and create another list, made of tuples
    with the clean title and the url. We add the prefix '_project' to
    title, and it's Scrapy's projects name, we prefix it '_spider' and
    it's Scrapy's spider name.
    We call the Scrapy project creation class on each element.
    """
    cwd = os.getcwd()
    urls2 = "/home/mic/python/cli_apps/cli_apps/newtags/urls2"
    url_files = os.listdir(urls2)

    urllst = []
    for file in url_files:
        with open(f"{urls2}/{file}", "r") as f:
            dirty_title = file[:-4]
            clean_title = dirty_title.replace("-", "_")
            title = clean_title.replace(".", "_")
            dirty_url = f.read()
            url = dirty_url.strip()
            urllst.append((title, url))

    for url in urllst:
        title = url[0]
        url = url[1]
        projname = f"{title}_project"
        spidername = f"{title}_spider"

        scrapyproj = ScrapyProject(projname, spidername, url)
        scrapyproj.project_creation()
        scrapyproj.settings_definition()
        scrapyproj.spider()


if __name__ == "__main__":
    project_creation()
