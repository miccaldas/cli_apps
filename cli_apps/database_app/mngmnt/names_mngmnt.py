"""
Module Docstring
"""
import os
import pickle

# import snoop
from cli_apps.database_app.methods import input_decision

from mngmnt.column_content import column_content
from mngmnt.get import get
from mngmnt.show_column import show_column
from mngmnt.sql_expression import sql_expression

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def names_mngmnt(names):
    """
    Calls all functions regarding names.
    """
    if names:
        with open("names.bin", "wb") as f:
            pickle.dump(names, f)

        sql_expression("names.bin", "nqy.bin")
        get("nqy.bin", "nlst.bin")
    else:
        question = input_decision("Do you want to see a list of names?[y/n]? ")
        if question == "y":
            column_content("SELECT name FROM cli_apps", "allnm.bin")
            show_column(
                "allnm.bin",
                "Choose Some Names!",
                "names.bin",
            )
            sql_expression("names.bin", "nqy.bin")
            get("nqy.bin", "nlst.bin")

            os.remove("names.bin")
            os.remove("nqy.bin")
            os.remove("allnm.bin")


if __name__ == "__main__":
    names_mngmnt()
