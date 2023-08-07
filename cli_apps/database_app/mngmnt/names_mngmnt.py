"""
Module Docstring
"""
import os
import pickle
from dotenv import load_dotenv

# import snoop
from cli_apps.database_app.methods import input_decision

from mngmnt.column_content import column_content
from mngmnt.get import get
from mngmnt.show_column import show_column
from mngmnt.sql_expression import sql_expression

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
load_dotenv()


# @snoop
def names_mngmnt(names):
    """
    Calls all functions regarding names.
    """
    da = os.getenv("da")

    if names:
        with open(f"{da}names.bin", "wb") as f:
            pickle.dump(names, f)

        sql_expression(f"{da}names.bin", f"{da}nqy.bin")
        get(f"{da}nqy.bin", f"{da}nlst.bin")
    else:
        question = input_decision("Do you want to see a list of names?[y/n]? ")
        if question == "y":
            column_content("SELECT name FROM cli_apps", f"{da}allnm.bin")
            show_column(
                f"{da}allnm.bin",
                "Choose Some Names!",
                f"{da}names.bin",
            )
            sql_expression(f"{da}names.bin", f"{da}nqy.bin")
            get(f"{da}nqy.bin", f"{da}nlst.bin")

            os.remove(f"{da}names.bin")
            os.remove(f"{da}nqy.bin")
            os.remove(f"{da}allnm.bin")


if __name__ == "__main__":
    names_mngmnt()
