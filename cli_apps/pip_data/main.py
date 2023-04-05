"""
Module where we define the tasks
of the pip update process.
"""
import os
import subprocess

import click
import snoop
from crontab import CronTab

from cron import cron
from db_upld import db_upload
from delete import delete
from extract_file_info import extract_file_info
from query_builder import query_builder
from tags.kwd_creator import csv_cleaner, kwd_creator
from tags.project_creation import (
    name_change,
    project_creation,
    settings_definition,
    spider,
    xorg_urls,
)

# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def change_name():
    """
    We'll change the name of the 'names_linux.txt'
    file to 'old_names_linux.txt'. This way, when
    we update again, we'll have the names of the
    entries, and can discard all that we already
    processed.
    """
    cwd = os.getcwd()
    # os.rename(f"{cwd}/lists/names_linux.txt", f"{cwd}/lists/old_names_linux.txt")


if __name__ == "__main__":
    change_name()


@snoop
def run():
    """
    We call the initiation script to get a
    list of installed pip modules and separate
    them from version names. 'query_builder'
    iterates through the names and puts them in
    command 'pip show'. The output is kept in
    files. the 'extract_file_info', takes the
    three fields we're interested in, name,
    summary and location, and puts them in new
    files.
    'db_upload' will iterate through this files
    and, as is parsing them, it will upload them.
    """

    cmd0 = "/home/mic/python/cli_apps/cli_apps/initiation_scripts.sh"
    # subprocess.run(cmd0, shell=True)

    # query_builder()

    # extract_file_info()

    # project_creation()

    # settings_definition()

    # xorg_urls()

    # name_change()

    # spider()

    # As we're using multiprocessing in 'spider_runner', I can't call it from another module,
    # as it expects a list as an argument, and that list must be given by code under the
    # function end and before setting the pool. This is a workaround.
    # cmd = "python /home/mic/python/cli_apps/cli_apps/pip_data/tags/spider_runner.py"
    # subprocess.run(cmd, shell=True)

    # csv_cleaner()

    kwd_creator()

    # db_upload()

    # delete()

    # cron()


if __name__ == "__main__":
    run()
