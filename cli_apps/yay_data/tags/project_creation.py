"""
Creates the *Yay's Scrapy* project folder.
"""
import os
import pickle
import subprocess

import snoop
from mysql.connector import Error, connect
from ScrapeSearchEngine.ScrapeSearchEngine import Bing, Google, Startpage
from snoop import pp


# @snoop
def project_creation():
    """
    Project Creation for *Arch* packages.
    Runs *Scrapy's* command to start a project::

        scrapy startproject pip_project
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    cmd = "/home/mic/.local/bin/scrapy startproject yay_project"
    subprocess.run(cmd, cwd=tags, shell=True)


if __name__ == "__main__":
    project_creation()


# @snoop
def settings_definition():
    """
    Settings definition for *Arch* packages.
    Defines the following options:\n
    1. FEED_EXPORT_FIELDS.  Title of the csv columns.
    2.  FEED_FORMAT. *csv*.
    3. FEED_URI.  *results.csv*
    4. RETRY_TIMES   Number of retries when there's a connection error.\n
    .. NOTE:: The feeds definitions will be deprecated in the near future.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    with open(f"{tags}/yay_project/yay_project/settings.py", "a") as d:
        d.write(
            "FEEDS = {'results.csv': {'format': 'csv', 'fields': ['name', 'content'],},}\n"
        )
        d.write("RETRY_TIMES = 1\n")


if __name__ == "__main__":
    settings_definition()


@snoop
def null_entries():
    """
    Sometimes there's entries in the database that don't have
    tag values. This function collects them and adds them to
    our list.\n
    .. code-block:: sql

        SELECT * FROM cli_apps WHERE t2 IS NULL
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    namesfile = "/home/mic/python/cli_apps/cli_apps/yay_data/newnames.bin"

    with open(namesfile, "rb") as f:
        newnames = pickle.load(f)

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="cli_apps"
        )
        cur = conn.cursor()
        query = "SELECT * FROM cli_apps WHERE t2 IS NULL"
        cur.execute(query)
        recs = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    records = [(b, c, e) for a, b, c, d, e, f, g, h, i in recs]
    for record in records:
        newnames += [record]
    with open(f"{tags}/newestnames.bin", "wb") as v:
        pickle.dump(newnames, v)


if __name__ == "__main__":
    null_entries()


@snoop
def xorg_urls():
    """
    Xorg_urls for Yay packages.
    All Xorg packages had as URL, a generic *Freedesktop* site
    url, which won't bring much information. We replace them
    with url's to their *Github* pages.
    """

    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    namesfile = "/home/mic/python/cli_apps/cli_apps/yay_data/tags/newestnames.bin"

    with open(namesfile, "rb") as f:
        newnames = pickle.load(f)

    newurls = []
    for entry in newnames:
        if entry[2] == "https://xorg.freedesktop.org/":
            if entry[0].startswith("xorg-"):
                newurl = f"https://github.com/freedesktop/{entry[0]}"
            else:
                newurl = f"https://github.com/freedesktop/xorg-{entry[0]}"
            newurls.append((entry[0], entry[1], newurl))
        else:
            newurls.append(entry)

    with open(f"{tags}/newurls.bin", "wb") as v:
        pickle.dump(newurls, v)


if __name__ == "__main__":
    xorg_urls()


@snoop
def alternative_urls():
    """
    There are some url's that don't produce scraping results,
    we look for them in *newurls.bin* and search the web for
    alternatives that we know will yield results. If we find
    them, we alter the url value.
    """

    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    with open(f"{tags}/newurls.bin", "rb") as f:
        newurls = pickle.load(f)

    changers = [
        i
        for i in newurls
        if i[2].startswith("https://gitlab.com")
        or i[2].startswith("https://pagure.io")
        or i[2].startswith("/")
        or "sourceforge" in i[2]
        or "canonware" in i[2]
    ]

    userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

    nurls = []
    if changers != []:
        for i in changers:
            name = i[0]
            startpage = Startpage(name, userAgent)
            if i[0].startswith("python-"):
                nm = i[0][7:]
                name = f"{nm} python"
                startpage = Startpage(name, userAgent)
            for s in startpage:
                if s.startswith("https://github.com"):
                    nurls.append((i[0], i[1], s))
                    break
                elif s.startswith("https://pypi.org"):
                    nurls.append((i[0], i[1], s))
                    break
                elif name in s:
                    nurls.append((i[0], i[1], s))
                    break

    for n in range(len(newurls)):
        for nu in range(len(nurls)):
            if newurls[n][0] == nurls[nu][0]:
                newurls.pop(n)
                newurls += [nurls[nu]]

    with open(f"{tags}/alturls.bin", "wb") as f:
        pickle.dump(newurls, f)


if __name__ == "__main__":
    alternative_urls()


@snoop
def name_change():
    """
    Name change for *Arch* packages.
    Some of these names have dashes and dots on them, and Scrapy
    doesn't accept them on its spider's/project's names.
    To comply, but not forget original name, we add a chenged
    version, with underline, as first element of the tuple.\n
    """

    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    with open(f"{tags}/alturls.bin", "rb") as f:
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
    For each entry in our packages list is built a spider, with its own file.\n
    :var str srch_title: Css query for *<h1>* elements.\n
    :var str enphasys: Css query for <em> tags. Usually sub-titles.\n
    :var str srch_text: Css query for all *<p>* tags.\n
    :var str name: The name of the package. Added so we can identify the lines in the csv.
    """

    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    with open(f"{tags}/newname.bin", "rb") as f:
        newurls = pickle.load(f)
    for entry in newurls:
        spider_name = f"{entry[0].strip()}_spider"
        class_name = f"{spider_name}".upper()
        with open(
            f"{tags}/yay_project/yay_project/spiders/{spider_name}.py",
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
