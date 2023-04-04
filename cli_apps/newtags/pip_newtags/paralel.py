"""
Module Docstring
"""
import os
import pickle
import subprocess
from multiprocessing import Pool

import snoop
from mysql.connector import Error, connect
from snoop import pp
from timebudget import timebudget


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def get_missing():
    """"""
    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="cli_apps"
        )
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


# if __name__ == "__main__":
#     get_missing()


@timebudget
@snoop
def noparalel():
    """"""
    sampledata = [
        ("watchdog", "https://pypi.org/project/watchdog"),
        ("tinyxml2", "https://github.com/leethomason/tinyxml2"),
        ("python-docutils", "https://docutils.sourceforge.io"),
        ("libtracefs", "https://github.com/rostedt/libtracefs"),
        ("libtraceevent", "https://github.com/rostedt/libtraceevent"),
        ("libmms", "https://www.unix.com/man-page/opensolaris/3lib/libmms/"),
        ("libbs2b", "https://github.com/alexmarsev/libbs2b"),
        ("pbzip2", "https://linux.die.net/man/1/pbzip2"),
        ("xautomation", "https://linux.die.net/man/7/xautomation"),
        ("evtest", "https://manpages.ubuntu.com/manpages/trusty/man1/evtest.1.html"),
        ("iproute2", "https://github.com/shemminger/iproute2"),
        ("libtirpc", "https://github.com/alisw/libtirpc"),
    ]

    cwd = os.getcwd()
    cmd = "scrapy startproject noparalel"
    subprocess.run(cmd, shell=True)

    with open("noparalel/noparalel/settings.py", "a") as d:
        d.write('FEED_EXPORT_FIELDS = ["name", "content"]')
        d.write("\n")
        d.write('FEED_FORMAT = "csv"')
        d.write("\n")
        d.write('FEED_URI = "results.csv"')
        d.write("\n")
        d.write("RETRY_TIMES = 1\n")
        d.close()

    for d in sampledata:
        spider_name = f"{d[0]}_spider"
        class_name = f"{spider_name}".upper()
        with open(
            f"noparalel/noparalel/spiders/{spider_name}.py",
            "w",
        ) as f:
            f.write("import scrapy\n")
            f.write("#import snoop\n")
            f.write("\n\n")
            f.write(f"class {class_name}(scrapy.Spider):\n")
            f.write(f"    name = '{spider_name}'\n")
            f.write("\n")
            f.write(f"    start_urls = ['{d[1]}']")
            f.write("\n\n")
            f.write("    #@snoop\n")
            f.write("    def parse(self, response):\n")
            f.write("        srch_title = response.css('h1::text').getall()\n")
            f.write("        srch_enphasys = response.css('em::text').getall()\n")
            f.write("        srch_text = response.css('p::text').getall()\n\n")
            f.write(f"        name = '{d[0]}'\n")
            f.write("        lsts = srch_title + srch_enphasys + srch_text\n")
            f.write("        results = {'name': name, 'content': lsts}\n")
            f.write("        yield results\n")


# if __name__ == "__main__":
#     noparalel()


@snoop
def paralel(input_index):
    """"""
    sampledata = [
        ("watchdog", "https://pypi.org/project/watchdog"),
        ("tinyxml2", "https://github.com/leethomason/tinyxml2"),
        ("python-docutils", "https://docutils.sourceforge.io"),
        ("libtracefs", "https://github.com/rostedt/libtracefs"),
        ("libtraceevent", "https://github.com/rostedt/libtraceevent"),
        ("libmms", "https://www.unix.com/man-page/opensolaris/3lib/libmms/"),
        ("libbs2b", "https://github.com/alexmarsev/libbs2b"),
        ("pbzip2", "https://linux.die.net/man/1/pbzip2"),
        ("xautomation", "https://linux.die.net/man/7/xautomation"),
        ("evtest", "https://manpages.ubuntu.com/manpages/trusty/man1/evtest.1.html"),
        ("iproute2", "https://github.com/shemminger/iproute2"),
        ("libtirpc", "https://github.com/alisw/libtirpc"),
    ]

    cwd = os.getcwd()
    cmd = "scrapy startproject paralel"
    subprocess.run(cmd, shell=True)

    with open("paralel/paralel/settings.py", "a") as d:
        d.write('FEED_EXPORT_FIELDS = ["name", "content"]')
        d.write("\n")
        d.write('FEED_FORMAT = "csv"')
        d.write("\n")
        d.write('FEED_URI = "results.csv"')
        d.write("\n")
        d.write("RETRY_TIMES = 1\n")
        d.close()

    for d in sampledata:
        spider_name = f"{d[0]}_spider"
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
            f.write(f"    start_urls = ['{d[1]}']")
            f.write("\n\n")
            f.write("    #@snoop\n")
            f.write("    def parse(self, response):\n")
            f.write("        srch_title = response.css('h1::text').getall()\n")
            f.write("        srch_enphasys = response.css('em::text').getall()\n")
            f.write("        srch_text = response.css('p::text').getall()\n\n")
            f.write(f"        name = '{d[0]}'\n")
            f.write("        lsts = srch_title + srch_enphasys + srch_text\n")
            f.write("        results = {'name': name, 'content': lsts}\n")
            f.write("        yield results\n")


# @snoop
# @timebudget
# def run(operation, input, pool):
#     pool.map(operation, input)


# processes_count = 8


# if __name__ == "__main__":
#     processes_pool = Pool(processes_count)
#     run(paralel, range(8), processes_pool)


@snoop
def run_spider(input_index):
    fldr = f"{os.getcwd()}/paralel/paralel/spiders"
    lstfls = os.listdir(fldr)

    for file in lstfls:
        cmd = f"scrapy crawl {file[:-3]}"
        subprocess.run(cmd, cwd=f"{os.getcwd()}/paralel/", shell=True)


@snoop
@timebudget
def run(operation, input, pool):
    pool.map(operation, input)


processes_count = 8


if __name__ == "__main__":
    processes_pool = Pool(processes_count)
    run(run_spider, range(8), processes_pool)
