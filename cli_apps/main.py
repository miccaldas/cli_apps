"""Module Docstring"""
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
import click
from crontab import CronTab
from build_url_list import build_url_list
from main_scrapy import main_scrapy
from mv_files import mv_files
from run_spider import apps_cli
from db_upload import db_upload
from pip_links_upld import links_upload

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def main():

    cmd = "./initiation_scripts.sh"
    subprocess.run(cmd, shell=True)
    build_url_list()
    main_scrapy()
    apps_cli()
    mv_files()
    cmd = "/home/mic/python/cli_apps/cli_apps/clean_files/sed_scripts.sh"
    subprocess.run(cmd, shell=True)
    # db_upload()
    # links_upld.py
    cron = CronTab("mic")
    dunst = "/usr/bin/dunstify"
    job = cron.new(command=f'{dunst} "cli_apps has updated and waits inspection."')
    job.minute.every(59)
    cron.write()


if __name__ == "__main__":
    main()
