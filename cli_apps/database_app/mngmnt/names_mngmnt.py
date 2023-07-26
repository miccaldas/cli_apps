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

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def names_expression():
    """
    Builds the SQL statement that'll look for data on
    the chosen names.
    """
    with open("names.bin", "rb") as g:
        names = pickle.load(g)
    nqry = []
    for i in names:
        partial = f"SELECT * FROM cli_apps WHERE name = '{i}'"
        nqry.append(partial)
        nqry.append(" UNION ")
    nqry.pop(-1)
    nqry.append(" ORDER BY TIME")
    nqy = " ".join(nqry)
    with open("nqy.bin", "wb") as f:
        pickle.dump(nqy, f)


if __name__ == "__main__":
    names_expression()


# @snoop
def get_names():
    """
    With the built expression on 'names_expression',
    we'll maake a db call and get the information.
    """
    with open("nqy.bin", "rb") as f:
        query = pickle.load(f)

    print(query)

    ninfo = dbdata(query, "fetch")

    with open("nlst.bin", "wb") as g:
        pickle.dump(ninfo, g)


if __name__ == "__main__":
    get_names()


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

        names_expression()
        get_names()
    else:
        question = input_decision("Do you want to see a list of names?[y/n]? ")
        if question == "y":
            all_names()
            show_names()
            names_expression()
            get_names()
            os.remove("allnm.bin")
            os.remove("names.bin")
            os.remove("nqy.bin")


if __name__ == "__main__":
    names_mngmnt()
