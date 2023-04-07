"""
Enters the Scrapy project folder and runs its spiders.
"""
import multiprocessing
import os
import subprocess
from multiprocessing import Pool

import snoop
from snoop import pp


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


@snoop
def spider_runner(spiders_lst):
    """
    .. code-block::

        scrapy crawl <sipder_name>

    We use multiprocessing to speed up the process.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    cmd = f"/home/mic/.local/bin/scrapy crawl {spiders_lst[:-3]}"
    subprocess.run(cmd, cwd=f"{tags}/yay_project/", shell=True)


if __name__ == "__main__":
    spiders_fldr = "/home/mic/python/cli_apps/cli_apps/yay_data/tags/yay_project/yay_project/spiders"
    spiderslst = os.listdir(spiders_fldr)
    spiders_lst = [i for i in spiderslst if i != "__init__.py"]
    with Pool() as pool:
        pool.map(spider_runner, spiders_lst)
