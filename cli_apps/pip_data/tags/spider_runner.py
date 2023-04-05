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


@snoop
def spider_runner(spiders_lst):
    """
    :var str cmd: *scrapy crawl <sipder_name>*\n
    We use multiprocessing to speed up the process.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data"
    if spiders_lst != "__init__.py":
        cmd = f"scrapy crawl {spiders_lst[:-3]}"
        subprocess.run(cmd, cwd=f"{pip}/yay_project/", shell=True)


if __name__ == "__main__":
    spiders_fldr = "/home/mic/python/cli_apps/cli_apps/pip_data/yay_project/yay_project/spiders"
    spiders_lst = os.listdir(spiders_fldr)
    with Pool() as pool:
        pool.map(spider_runner, spiders_lst)
