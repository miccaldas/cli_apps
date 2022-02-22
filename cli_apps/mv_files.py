"""
Module that will get information from the
files in the spider folders and add the
url data to the bunch.
"""
import json
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def mv_files():
    """
    We'll use 'os' to get us inside the
    the directories in 'spider_folders',
    get the information to a list of
    tuples, to which we'll add the url value.
    """

    cwd = os.getcwd()
    os.chdir(f"{cwd}/spider_folders/")
    path = "/home/mic/python/cli_apps/cli_apps/spider_folders/"

    with open(f"{cwd}/lists/pypi/urls_pip.txt", "r") as f:
        urls = f.readlines()

    jslist = []
    for d in os.listdir(path):
        print(d)
        if "results.csv" in os.listdir(f"{path}{d}"):
            if os.path.getsize(f"{path}{d}/results.csv") != 0:
                with open(f"{path}{d}/results.csv", "r") as f:
                    data = f.readlines()
                    jslist.append((f"{d[:-7]}", f"{data}"))
        os.chdir("../")
    print(jslist[1])
    print(jslist[1][1])
    print(type(jslist[1][1]))
    print(jslist[1][1][0])
    print(type(jslist[1][1][0]))

    slist = []
    tlist = []
    url1 = []
    for i in range(len(jslist)):
        it = jslist[i][1]
        print(it)
        slist.append(jslist[i][0])
        print(jslist[i][0])
        tlist.append(it)
        namebreak = f"{jslist[i][0]}\n"
        print(namebreak)
        name = [v for v in urls if os.path.basename(os.path.normpath(f"{v}")) == namebreak]
        for n in name:
            url1.append(str(n))

    print(slist)
    print(tlist)
    print(url1)
    zipe = list(zip(slist, tlist, url1))
    print(zipe)

    with open("/home/mic/python/cli_apps/cli_apps/clean_files/spider_results.txt", "a") as f:
        for i in zipe:
            f.write(f"{i}")
            f.write("\n")


if __name__ == "__main__":
    mv_files()
