"""
Houses all functions regarding keywords.
"""
import os
import pickle

# import snoop
from cli_apps.database_app.db import dbdata
from cli_apps.database_app.methods import input_decision

from mngmnt.column_content import column_content
from mngmnt.get import get
from mngmnt.show_column import show_column
from mngmnt.sql_expression import sql_expression

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
# fzf = FzfPrompt()


# @snoop
def kwd_mngmnt(keywords):
    """
    Module that aggregates all operations regarding keywords.
    If the user supplied some, we'll treat them to get all
    entries with that tags. If not, we ask if he wants to see
    a list of keywords. If the user agrees and chooses some tags,
    we'll analyze them also.
    """
    if keywords:
        with open("keywords.bin", "wb") as g:
            pickle.dump(keywords, g)
        sql_expression("keywords.bin", "kquery.bin")
        get("kquery.bin", "klst.bin")
        os.remove("kquery.bin")
        os.remove("keywords.bin")
    else:
        choice = input_decision("Do you want to see a list of available tags[y/n]? ")
        if choice == "y":
            column_content(
                "SELECT t1 FROM cli_apps UNION SELECT t2 FROM cli_apps UNION SELECT t3 FROM cli_apps UNION SELECT t4 FROM cli_apps",
                "klst.bin",
            )
            show_column(
                "klst.bin",
                "Choose Some Tags!",
                "keywords.bin",
            )
            sql_expression("keywords.bin", "kquery.bin")
            get("kquery.bin", "klst.bin")
            os.remove("kquery.bin")
            os.remove("chc.bin")
            os.remove("keywords.bin")
        else:
            os.remove("chc.bin")


if __name__ == "__main__":
    kwd_mngmnt()
