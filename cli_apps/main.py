"""
Module where we define the tasks
of the pip update process.
"""

import os
import subprocess

import click
import isort  # noqa: F401
import snoop
from crontab import CronTab
from loguru import logger

from db_upld import db_upload
from delete import delete
from query_builder import query_builder

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def change_name():
    """
    We'll change the name of the 'names_linux.txt'
    file to 'old_names_linux.txt'. This way, when
    we update again, we'll have the names of the
    entries, and can discard all that we already
    processed.
    """
    cwd = os.getcwd()
    os.rename(f"{cwd}/lists/names_linux.txt", f"{cwd}/lists/old_names_linux.txt")


if __name__ == "__main__":
    change_name()


@logger.catch
@snoop
def run():
    """
    We call the initiation script to get a
    list of installed pip modules and separate
    them from version names. 'query_builder'
    iterates through the names and puts them in
    command 'pip show'. The output is kept in
    files. the 'extract_file_info', takes the
    three fields we're inteersted in, name,
    summary and location, and puts them in new
    files.
    'db_upload' will iterate through this files
    and, as is parsing them, it will upload them.
    """

    cmd0 = "/home/mic/python/cli_apps/cli_apps/initiation_scripts.sh"
    subprocess.run(cmd0, shell=True)

    query_builder()

    cmd1 = "/home/mic/python/cli_apps/cli_apps/extract_file_info.sh"
    subprocess.run(cmd1, shell=True)

    db_upload()

    # delete()


if __name__ == "__main__":
    run()


@logger.catch
@snoop
def dunst():
    """
    We'll use the code of the todo's
    app, to send a message, saying
    that pip update was done and
    iinputed to the db.
    """

    cron = CronTab("mic")
    dunst = "/usr/bin/dunstify"
    job = cron.new(command=f'{dunst} "cli_apps pip has updated and uploaded to the db."')
    job.minute.every(59)
    cron.write()


if __name__ == "__main__":
    dunst()
