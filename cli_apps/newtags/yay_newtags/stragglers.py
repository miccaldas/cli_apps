"""
These are some fourty/fifty entries that their url value is 404 or
otherwise unavailable. Because of this, they have no tags values.
We'll manually insert new url's, and get them new tags.
"""
import csv
import os
import pickle
import re
import subprocess
from multiprocessing import Pool

import snoop
from keybert import KeyBERT
from mysql.connector import Error, connect
from snoop import pp
from thefuzz import fuzz, process


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def get_missing():
    """
    Gets all the entries in the database that don't have any tags.\n
    """
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT * FROM cli_apps WHERE t2 = 'NA'"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    with open("records.bin", "wb") as f:
        pickle.dump(records, f)


if __name__ == "__main__":
    get_missing()


@snoop
def missing_list():
    """
    List with names and new url values to upload to the database.
    """

    newlst = [
        ("liborcus", "https://github.com/Distrotech/liborcus"),
        ("libnewt", "https://pagure.io/newt"),
        ("volume_key", "https://linux.die.net/man/8/volume_key"),
        (
            "linux-firmware-whence",
            "https://github.com/cernekee/linux-firmware/blob/master/WHENCE",
        ),
        ("licloudproviders", "https://libcloud.apache.org"),
        ("dmraid", "https://linux.die.net/man/8/dmraid"),
        ("ipsolve", "https://lpsolve.sourceforge.net/5.5/"),
        ("liburing", "https://github.com/axboe/liburing"),
        ("gcr", "https://gitlab.gnome.org/GNOME/gcr"),
        ("zsh", "https://zsh.sourceforge.io"),
        ("mailcap", "https://linux.die.net/man/4/mailcap"),
        ("pixman", "http://www.pixman.org"),
        (
            "dnssec-anchors",
            "https://dnsinstitute.com/documentation/dnssec-guide/ch03s04.html",
        ),
        ("libxslt", "http://www.xmlsoft.org/libxslt/index.html"),
        ("sysfsutils", "https://github.com/linux-ras/sysfsutils"),
        ("npm", "https://docs.npmjs.com/about-npm"),
        ("libnotify", "https://github.com/GNOME/libnotify"),
        ("libssh2", "https://github.com/libssh2/libssh2"),
        ("mdadm", "https://linux.die.net/man/8/mdadm"),
        ("libixion", "https://github.com/Distrotech/libixion"),
        ("keyutils", "https://man7.org/linux/man-pages/man7/keyutils.7.html"),
        ("libgsf", "https://github.com/GNOME/libgsf"),
        ("libxml2", "https://gitlab.gnome.org/GNOME/libxml"),
        ("linux-firmware", "https://github.com/endlessm/linux-firmware"),
        ("libcap", "https://man7.org/linux/man-pages/man3/libcap.3.html"),
        ("wavcap", "https://github.com/AyrA/wavCap"),
        (
            "xcb-util-cursor",
            "https://www.linuxfromscratch.org/blfs/view/svn/x/xcb-util-cursor.html",
        ),
        ("ttf-roboto", "https://befonts.com/roboto-font-family.html"),
        ("nano", "https://www.nano-editor.org/dist/latest/nano.html"),
    ]

    with open("newlst.bin", "wb") as f:
        pickle.dump(newlst, f)


if __name__ == "__main__":
    missing_list()


@snoop
def start_project():
    """
    Starts a *Scrapy* project, using the command::

        scrapy startproject paralel
    """
    cwd = os.getcwd()
    cmd = "scrapy startproject paralel"
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    start_project()


@snoop
def create_settings(records):
    """
    Adds personal settings to the *Scrapy* document.\n
    We'll use multiprocessing to speed up the build.\n
    .. note::
        For multiprocessing to work, the data source must be
        outside the function. The *Pool* class creates one worker per cpu
        and calls the function with *map*. Notice that, when the data is
        fed to the function, *records* doesn't stand for a list of tuples,
        but only for one tuple at a time.
    """

    with open("paralel/paralel/settings.py", "a") as d:
        d.write('FEED_EXPORT_FIELDS = ["name", "content"]')
        d.write("\n")
        d.write('FEED_FORMAT = "csv"')
        d.write("\n")
        d.write('FEED_URI = "results.csv"')
        d.write("\n")
        d.write("RETRY_TIMES = 1\n")
        d.close()

    spider_name = f"{records[0]}_spider"
    class_name = f"{spider_name}".upper()
    with open(
        f"paralel/paralel/spiders/{spider_name}.py",
        "w",
    ) as f:
        f.write("import scrapy\n")
        f.write("#import snoop\n")
        f.write("\n\n")
        f.write(f"class {class_name}(scrapy.Spider):\n")
        f.write(f"    name = '{spider_name}'\n")
        f.write("\n")
        f.write(f"    start_urls = ['{records[1]}']")
        f.write("\n\n")
        f.write("    #@snoop\n")
        f.write("    def parse(self, response):\n")
        f.write("        srch_title = response.css('h1::text').getall()\n")
        f.write("        srch_enphasys = response.css('em::text').getall()\n")
        f.write("        srch_text = response.css('p::text').getall()\n\n")
        f.write(f"        name = '{records[0]}'\n")
        f.write("        lsts = srch_title + srch_enphasys + srch_text\n")
        f.write("        results = {'name': name, 'content': lsts}\n")
        f.write("        yield results\n")


if __name__ == "__main__":
    with open("newlst.bin", "rb") as f:
        records = pickle.load(f)
    with Pool() as pool:
        pool.map(create_settings, records)


@snoop
def run_spider(lstfls):
    """
    Runs the newly created spiders.\n
    Uses the command::

        scrapy crawl <spider_name>\n
    Function ran with multiprocessing.
    """

    cmd = f"scrapy crawl {lstfls[:-3]}"
    subprocess.run(cmd, cwd=f"{os.getcwd()}/paralel/", shell=True)


if __name__ == "__main__":
    fldr = f"{os.getcwd()}/paralel/paralel/spiders"
    lstfls = os.listdir(fldr)
    with Pool() as pool:
        pool.map(run_spider, lstfls)


@snoop
def csv_cleaning():
    """
    The column names were repeated for each entry, we remove them here.
    We remove also the excess whitespaces from the scraped content.
    """

    lines = []
    with open(f"{os.getcwd()}/paralel/results.csv", "r") as r:
        reader = csv.reader(r)
        for line in reader:
            lines.append(line)

    content = [i for i in lines if i != ["name", "content"]]

    nospaces = []
    for k in range(len(content)):
        try:
            pattern = re.sub("\s+", " ", content[k][1])
        except IndexError:
            pass
        nospaces.append([content[k][0], pattern])

    with open("nospaces.bin", "wb") as f:
        pickle.dump(nospaces, f)


if __name__ == "__main__":
    csv_cleaning()


@snoop
def kwd_creation(content):
    """
    Creates and cleans tags taken  from the collected scrapings.
    Function run with multiprocessing.
    """

    name = content[0]
    text = content[1]
    kw_model = KeyBERT()
    keys = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 1),
        stop_words=[f"{name}", f"n{name}", "codespaces", "codespace", "pages"],
    )
    keywords = [o for o, p in keys]

    kwds = []
    for y in keywords:
        slst = [b for b in keywords if b != y]
        if slst != []:
            value = process.extractOne(y, slst)
            if value[1] < 80:
                kwds.append(y)
    similars = [u for u in keywords if u not in kwds]
    if similars != []:
        sim_choice = max(similars, key=len)
        kwds += [sim_choice]
    with open(f"kws/{name}", "w") as v:
        for q in kwds:
            v.write(f"{q}\n")


if __name__ == "__main__":
    with open("nospaces.bin", "rb") as f:
        content = pickle.load(f)
    with Pool() as pool:
        pool.map(kwd_creation, content)


@snoop
def kwd_upload():
    """
    Gathers the tags values, uploads them to the database.
    """

    fldr = f"{os.getcwd()}/kws"
    filelst = os.listdir(fldr)

    taglst = []
    for f in filelst:
        with open(f"{fldr}/{f}", "r") as g:
            tags = g.readlines()
            taglst.append((f"{f}", tags))

    entries = []
    for entry in taglst:
        if len(entry[1]) >= 3:
            t2 = entry[1][0].strip()
            t3 = entry[1][1].strip()
            t4 = entry[1][2].strip()
            entries.append((entry[0], t2, t3, t4))
        if len(entry[1]) == 2:
            t2 = entry[1][0].strip()
            t3 = entry[1][1].strip()
            t4 = "NA"
            entries.append((entry[0], t2, t3, t4))
        if len(entry[1]) == 1:
            t2 = entry[1][0].strip()
            t3 = "NA"
            t4 = "NA"
            entries.append((entry[0], t2, t3, t4))
        if entry[1] == []:
            t2 = "NA"
            t3 = "NA"
            t4 = "NA"
            entries.append((entry[0], t2, t3, t4))

    try:
        for e in entries:
            answers = [e[1], e[2], e[3], e[0]]
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "UPDATE cli_apps SET t2 = %s, t3 = %s, t4 = %s WHERE name = %s"
            cur.execute(query, answers)
            conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    kwd_upload()
