"""
Main module. Calls all other modules.
"""
import snoop
from cli_apps.yay_data.cront import crons
from cli_apps.yay_data.db_upld import db_upload, kwd_collector
from cli_apps.yay_data.delete import delete
from cli_apps.yay_data.kwd_creator import kwd_creator
from cli_apps.yay_data.lists_test import yay_lst

# from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def main():
    """
    We call the other modules, in order, to update the database.
    The program runs as much as needed to verify if there are new
    packages. This question is answered in *yay_names*. If
    *yay_names* is an empty list, it'll return *n*, if it's not,
    it'll return nothing. We check for the return of "yay_names*
    to see if we should continue.
    """
    yay = "/home/mic/python/cli_apps/cli_apps/yay_data/"

    yay_lst()
    # lsts.db_lst()
    # yn = lsts.yay_names()

    # if yn != "n":
    #     kwd_creator()
    #     kwd_collector()
    #     db_upload()
    #     crons()
    #     delete()


if __name__ == "__main__":
    main()
