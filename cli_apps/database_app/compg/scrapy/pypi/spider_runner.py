"""
Enters the Scrapy project folder and runs its spiders.
"""
import multiprocessing
import os
import subprocess
from multiprocessing import Pool

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

# Environmental Variables
compg = f"{os.getcwd()}/"
project = f"{compg}compg_project/"
spiders = f"{project}compg_project/spiders/"


@snoop
def spider_runner(spiders_lst):
    """
    .. code-block::

        scrapy crawl <sipder_name>

    We use multiprocessing to speed up the process.
    """
    cmd = f"/usr/bin/scrapy crawl {spiders_lst[:-3]}"
    subprocess.run(cmd, cwd=project, shell=True)


if __name__ == "__main__":
    spiderslst = os.listdir(spiders)
    spiders_lst = [i for i in spiderslst if i != "__init__.py"]
    with Pool() as pool:
        pool.map(spider_runner, spiders_lst)
