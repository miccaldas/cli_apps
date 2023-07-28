"""
Module Docstring
"""
import os
import pickle
from time import sleep

# import snoop
from cli_apps.database_app.db import dbdata
from cli_apps.database_app.methods import input_decision
from pyfzf.pyfzf import FzfPrompt
from rich.console import Console
from rich.padding import Padding

from mngmnt.get import get
from mngmnt.sql_expression import sql_expression

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def all_names():
    """
    Collects all names in the database.
    """
    query = "SELECT name FROM cli_apps"
    alln = dbdata(query, "fetch")
    allnm = [i[0] for i in alln]

    with open("allnm.bin", "wb") as f:
        pickle.dump(allnm, f)


if __name__ == "__main__":
    all_names()


# @snoop
def show_names():
    """
    Shows the name list with fzf. The user might
    choose to select some.
    """
    fzf = FzfPrompt()

    with open("allnm.bin", "rb") as f:
        allnm = pickle.load(f)

    console = Console()
    console.print(
        Padding(
            "[bold #AAC8A7]Choose the names that interest you. If any.[/]",
            (2, 10, 2, 10),
        )
    )
    sleep(0.5)
    newnames = fzf.prompt(
        allnm,
        '--border bold --border-label="╢Choose Some Names!╟" --border-label-pos bottom',
    )
    if newnames != []:
        with open("names.bin", "wb") as g:
            pickle.dump(newnames, g)


if __name__ == "__main__":
    show_names()


# @snoop
def names_mngmnt(names):
    """
    Calls all functions regarding names.
    """
    console = Console()
    if names:
        with open("names.bin", "wb") as f:
            pickle.dump(names, f)

        sql_expression("names.bin", "nqy.bin")
        get("nqy.bin", "nlst.bin")
    else:
        question = input_decision("Do you want to see a list of names?[y/n]? ")
        if question == "y":
            all_names()
            show_names()
            sql_expression("names.bin", "nqy.bin")
            get("nqy.bin", "nlst.bin")

            os.remove("allnm.bin")
            os.remove("names.bin")
            os.remove("nqy.bin")


if __name__ == "__main__":
    names_mngmnt()
