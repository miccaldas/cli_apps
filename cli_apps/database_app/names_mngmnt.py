"""
Module Docstring
"""
import snoop
from snoop import pp
import pickle
from db import dbdata
import os
from time import sleep
from pyfzf.pyfzf import FzfPrompt


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
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


@snoop
def get_names():
    """
    With the built expression on 'names_expression',
    we'll maake a db call and get the information.
    """
    with open("nqy.bin", "rb") as f:
        query = pickle.load(f)

    print(query)

    ninfo = dbdata(query, "fetch")

    with open("ninfo.bin", "wb") as g:
        pickle.dump(ninfo, g)


@snoop
def all_names():
    """
    Collects all names in the database.
    """
    query = "SELECT name FROM cli_apps"
    alln = dbdata(query, "fetch")
    allnm = [i[0] for i in alln]

    with open("allnm.bin", "wb") as f:
        pickle.dump(allnm, f)


@snoop
def show_names():
    """
    Shows the name list with fzf. The user might
    choose to select some.
    """
    fzf = FzfPrompt()

    with open("allnm.bin", "rb") as f:
        allnm = pickle.load(f)

    print("Choose the names that interest you. If any.")
    sleep(0.5)
    newnames = fzf.prompt(
        allnm,
        '--border bold --border-label="╢Choose Some Names!╟" --border-label-pos bottom',
    )
    if newnames != []:
        newexp = names_expression(newnames)

    with open("names.bin", "wb") as g:
        pickle.dump(newexp, g)


@snoop
def names_mngmnt(names):
    """
    Calls all functions regarding names.
    """
    if names:
        with open("names.bin", "wb") as f:
            pickle.dump(names, f)

        names_expression()
        get_names()
    else:
        question = input("Do you want to see a list of names?[y/n]? ")
        if question == "y":
            all_names()
            show_names()
            names_expression()
            get_names()

    os.remove("names.bin")
    os.remove("nqy.bin")
    os.remove("allnm.bin")
