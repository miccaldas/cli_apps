"""
Enters each Scrapy project folder and runs its spider.
"""
# from configs.config import Efs, tput_config
import os
import subprocess

# import snoop
# from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def spider_runner():
    """"""
    cwd = os.getcwd()
    lst = os.listdir(cwd)
    scrapylst = [i for i in lst if i.endswith("_project")]

    for folder in scrapylst:
        spider = f"{folder[:-8]}_spider"
        cmd = f"scrapy crawl {spider}"
        subprocess.run(cmd, cwd=f"{cwd}/{folder}", shell=True)


if __name__ == "__main__":
    spider_runner()
