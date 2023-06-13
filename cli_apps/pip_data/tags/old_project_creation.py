"""
Creates the *Pip's Scrapy* project folder.
"""
import os
import pickle
import subprocess

import snoop
from snoop import pp


@snoop
def project_creation():
    """
    Project Creation for Pip packages.
    Runs *Scrapy's* command to start a project.\n
    :var str cmd: *scrapy startproject pip_project*.
    """
    cwd = os.getcwd()
    cmd = "/home/mic/.local/bin/scrapy startproject pip_project"
    subprocess.run(cmd, cwd=cwd, shell=True)


if __name__ == "__main__":
    project_creation()


@snoop
def settings_definition():
    """
    Settings Definition for Pip packages.
    Defines the following options:\n
    3. FEED_URI.  *results.csv*
    4. RETRY_TIMES   Number of retries when there's a connection error.\n
    .. NOTE:: The feeds definitions will be deprecated in the near future.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/pip_data/tags"
    with open(f"{tags}/pip_project/pip_project/settings.py", "a") as d:
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
    with open(f"{tags}/pip_project/pip_project/pipelines.py", "r") as f:
        lines = f.readlines()
    with open(f"{tags}/pip_project/pip_project/pipelines.py", "w") as f:
        for line in lines:
            f.write(line)
        f.write("\n")
        f.write("        return item")


if __name__ == "__main__":
    settings_definition()


@snoop
def xorg_urls():
    """
    Xorg_urls for Pip packages.
    All Xorg packages had as URL, a generic *Freedesktop* site
    url, which won't bring much information. We replace them
    with url's to their *Github* pages.
    """

    tags = "/home/mic/python/cli_apps/cli_apps/pip_data/tags"
    results = "/home/mic/python/cli_apps/cli_apps/pip_data/results"
    lstresults = os.listdir(results)

    newurls = []
    for file in lstresults:
        with open(f"{results}/{file}", "r") as f:
            result = f.readlines()
        if result[2] == "https://xorg.freedesktop.org/":
            if result[0].startswith("xorg-"):
                newurl = f"https://github.com/freedesktop/{result[0]}"
            else:
                newurl = f"https://github.com/freedesktop/xorg-{result[0]}"
            newurls.append((result[0], result[1], newurl))
        else:
            newurls.append(result)

    with open(f"{tags}/newurls.bin", "wb") as v:
        pickle.dump(newurls, v)


if __name__ == "__main__":
    xorg_urls()


@snoop
def name_change():
    """
    Name change for Pip packages.
    Some of these names have dashes and dots on them, and Scrapy
    doesn't accept them on its spider's/project's names.
    To comply, but not forget original name, we add a chenged
    version, with underline, as first element of the tuple.\n
    """

    tags = "/home/mic/python/cli_apps/cli_apps/pip_data/tags"
    with open(f"{tags}/newurls.bin", "rb") as f:
        setcols = pickle.load(f)

    dotname = [(h.replace(".", "_"), h, d, e) for h, d, e in setcols]
    newname = [(n.replace("-", "_"), i, o, m) for n, i, o, m in dotname]
    with open(f"{tags}/newname.bin", "wb") as v:
        pickle.dump(newname, v)


if __name__ == "__main__":
    name_change()


@snoop
def spider():
    """
    Spider creation for pip packages.
    For each entry in our packages list is built a spider, that'llhave its own file.\n
    :var str srch_title: Css query for *<h1>* elements.\n
    :var str enphasys: Css query for <em> tags. Usually sub-titles.\n
    :var str srch_text: Css query for all *<p>* tags.\n
    :var str name: The name of the package. Added so we can identify the lines in the csv.
    """

    tags = "/home/mic/python/cli_apps/cli_apps/pip_data/tags"
    with open(f"{tags}/newname.bin", "rb") as f:
        newurls = pickle.load(f)
    for entry in newurls:
        spider_name = f"{entry[0].strip()}_spider"
        class_name = f"{spider_name}".upper()
        with open(
            f"{tags}/pip_project/pip_project/spiders/{spider_name}.py",
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


if __name__ == "__main__":
    spider()
