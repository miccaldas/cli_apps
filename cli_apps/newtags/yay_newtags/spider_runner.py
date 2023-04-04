"""
Enters the Scrapy project folder and runs its spiders.
"""
import os
import subprocess

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def spider_runner():
    """
    :var str cmd: *scrapy crawl <sipder_name>*
    """
    spiders_fldr = f"{os.getcwd()}/yay_project/yay_project/spiders"
    spiders_lst = os.listdir(spiders_fldr)
    for sp in spiders_lst:
        if sp != "__init__.py":
            cmd = f"scrapy crawl {sp[:-3]}"
            subprocess.run(cmd, cwd=f"{os.getcwd()}/yay_project/", shell=True)


if __name__ == "__main__":
    spider_runner()
