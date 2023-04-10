"""
Main module. Calls all other modules.
"""
import sys

# Here so __pycache__ folders aren't created.
sys.dont_write_bytecode = True
import os
import pickle
import subprocess

# import snoop
from cli_apps.yay_data.cront import crons
from cli_apps.yay_data.db_upld import db_upload, kwd_collector
from cli_apps.yay_data.delete import delete
from cli_apps.yay_data.lists import Lists
from cli_apps.yay_data.tags.kwd_creator import csv_cleaner, kwd_creator
from cli_apps.yay_data.tags.project_creation import (
    alternative_urls,
    name_change,
    null_entries,
    project_creation,
    settings_definition,
    spider,
    xorg_urls,
)

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def main():
    """
    We call the other modules, in order, to update the database.
    The program runs as much as needed to ascertain two things:\n
    1. Is there new packages?
    2.  Is there packages in the db that need tag values?
        This questions are answered in the *yay_names* method and in
        the *null_entries* function, respectively. When the latter has
        run, we do a check to see if one of them created any output.
        We check this by seeing if the *bin* documents they create are
        not empty. If they aren't, the other modules are ran. If not, only
        the *delete* module will run.
    """

    lsts = Lists(
        "/home/mic/python/cli_apps/cli_apps/yay_data",
        "/home/mic/python/cli_apps/cli_apps/yay_data/lists",
    )
    lsts.yay_lst()
    lsts.db_lst()
    lsts.yay_names()

    project_creation()
    settings_definition()
    null_entries()

    yaydata = os.listdir("/home/mic/python/cli_apps/cli_apps/yay_data")
    tags = os.listdir("/home/mic/python/cli_apps/cli_apps/yay_data/tags")
    with open("/home/mic/python/cli_apps/cli_apps/yay_data/newnames.bin", "rb") as f:
        newnames = pickle.load(f)
    with open("/home/mic/python/cli_apps/cli_apps/yay_data/tags/newestnames.bin", "rb") as d:
        newestnames = pickle.load(d)

    if newnames != [] or newestnames != []:
        xorg_urls()
        alternative_urls()
        name_change()
        spider()
        # The module 'spider_runner' has multiprocessing on and can't be called as the
        # other modules. This is a work-around.
        cmd = f"/usr/bin/python {os.getcwd()}/tags/spider_runner.py"
        subprocess.run(cmd, shell=True)
        csv_cleaner()
        kwd_creator()
        kwd_collector()
        db_upload()
        crons()
    delete()


if __name__ == "__main__":
    main()
