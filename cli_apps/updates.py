"""Module Docstring"""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

from build_url_list import build_url_list
from main_scrapy import main_scrapy
from run_spider import apps_cli

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def teste():

    """cmd = "pip list --format freeze > first_pip.txt"
    subprocess.run(cmd, shell=True)
    cmd = "./sed_script.sh"
    subprocess.run(cmd, shell=True)
    build_url_list()
    main_scrapy()
    apps_cli()"""


if __name__ == "__main__":
    teste()
