"""
Module where we define the tasks
of the pip update process.
"""

import os
import subprocess

import click

# import snoop
from crontab import CronTab

from cron import cron
from db_upld import db_upload, kwd_collector
from delete import delete
from extract_file_info import extract_file_info
from initiation_scripts import db_data, initiation_scripts
from query_builder import query_builder
from tags.kwd_creator import csv_cleaner, kwd_creator
from tags.project_creation import init_project
from tags.spider_runner import spider_runner

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
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

    # db_data()
    initiation_scripts()

    # As we're using multiprocessing in 'query_builder', I can't call it from another module,
    # as it expects a list as an argument, and that list must be given by code under the
    # function but before setting the pool. This is a workaround.
    cmd = "python /home/mic/python/cli_apps/cli_apps/pip_data/query_builder.py"
    subprocess.run(cmd, shell=True)

    extract_file_info()

    # We check the 'results' folder to see if there's anything there.
    # If there is, we continue.
    cwd = os.getcwd()
    file_res = os.listdir(f"{cwd}/results")

    if file_res != []:
        init_project()
        spider_runner()
        csv_cleaner()
        kwd_creator()
        db_upload()
    delete()


if __name__ == "__main__":
    run()
