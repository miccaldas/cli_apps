"""
Module where we define the tasks
of the yay update process.
"""
import subprocess

import click
import isort  # noqa: F401
import snoop
from loguru import logger

from cront import crons
from db_upload import db_upload
from delete_transient_files import delete_transient_files
from natural_language import natural_language
from query_builder import query_builder

fmt = "{time} - {name} - {level} - {message}"
logger.add(
    "../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True
)  # noqa: E501
logger.add(
    "../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True
)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def tasks():
    """
    We call all the functions and scripts that
    source, treat, store and clean, the information
    regarding the packages installed by pacman and AUR.
    Aditionally it's created a notification to warn the
    user that the update has ran.
    """
    cmd = "/home/mic/python/cli_apps/cli_apps/yay_querying/yay_lst.sh"
    subprocess.run(cmd, shell=True)

    query_builder()

    cmd1 = "/home/mic/python/cli_apps/cli_apps/yay_querying/extract_file_info.sh"
    subprocess.run(cmd1, shell=True)

    db_upload()

    natural_language()

    delete_transient_files()
    crons()


if __name__ == "__main__":
    tasks()
