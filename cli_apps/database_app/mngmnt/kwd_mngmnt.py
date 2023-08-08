"""
Houses all functions regarding keywords.
"""
import os
import pickle

# import snoop
from cli_apps.database_app.db import dbdata
from cli_apps.database_app.methods import input_decision
from dotenv import load_dotenv
from snoop import pp

from mngmnt.column_content import column_content
from mngmnt.get import get
from mngmnt.show_column import show_column
from mngmnt.sql_expression import sql_expression


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
load_dotenv()


# @snoop
def kwd_mngmnt(keywords):
    """
    Module that aggregates all operations regarding keywords.
    If the user supplied some, we'll treat them to get all
    entries with that tags. If not, we ask if he wants to see
    a list of keywords. If the user agrees and chooses some tags,
    we'll analyze them also.
    """
    da = os.getenv("DA")

    if keywords:
        with open(f"{da}keywords.bin", "wb") as g:
            pickle.dump(keywords, g)
        sql_expression(f"{da}keywords.bin", f"{da}kquery.bin")
        get(f"{da}kquery.bin", f"{da}klst.bin")
        os.remove(f"{da}kquery.bin")
        os.remove(f"{da}keywords.bin")
    else:
        choice = input_decision("Do you want to see a list of available tags[y/n]? ")
        if choice == "y":
            column_content(
                "SELECT t1 FROM cli_apps UNION SELECT t2 FROM cli_apps UNION SELECT t3 FROM cli_apps UNION SELECT t4 FROM cli_apps",
                f"{da}klst.bin",
            )
            show_column(
                f"{da}klst.bin",
                "Choose Some Tags!",
                f"{da}keywords.bin",
            )
            sql_expression(f"{da}keywords.bin", f"{da}kquery.bin")
            get(f"{da}kquery.bin", f"{da}klst.bin")
            os.remove(f"{da}kquery.bin")
            os.remove(f"{da}keywords.bin")


if __name__ == "__main__":
    kwd_mngmnt()
