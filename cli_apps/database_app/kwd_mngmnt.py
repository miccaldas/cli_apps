"""
Houses all functions regarding keywords.
"""
import os
import pickle
from time import sleep

import snoop
from pyfzf.pyfzf import FzfPrompt
from snoop import pp

from db import dbdata


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])
fzf = FzfPrompt()


@snoop
def kwds_expression():
    """
    Searches the tag fields for each of the chosen keywords.
    Creates an UNION SQL query between results of each tags.
    This precludes repeated results. The SQL query is kept
    in a pickle file.
    """
    with open("keywords.bin", "rb") as g:
        keys = pickle.load(g)

    qry = []
    for i in keys:
        query = f"SELECT * FROM cli_apps WHERE t1 = '{i}' OR t2 = '{i}' OR t3 = '{i}' OR t4 = '{i}'"
        qry.append(query)
    querytups = [(g, " UNION ") for g in qry]
    querylst = [h for tup in querytups for h in tup]
    querylst.pop(-1)
    query = " ".join(querylst)

    with open("kquery.bin", "wb") as f:
        pickle.dump(query, f)


if __name__ == "__main__":
    kwds_expression()


@snoop
def get_kwds():
    """
    Uses the expression created by 'kwds_expression' to make
    a database call. Keeps results in a pickle file.
    """
    with open("kquery.bin", "rb") as f:
        query = pickle.load(f)

    kl = dbdata(query, "fetch")

    with open("klst.bin", "wb") as g:
        pickle.dump(kl, g)


if __name__ == "__main__":
    get_kwds()


@snoop
def kwdchoice():
    """
    Where we ask the user that did not input tags,
    if he wants to see a list of them.
    """
    chc = input("Do you want to see a list of available tags[y/n]? ")
    with open("chc.bin", "wb") as f:
        pickle.dump(chc, f)


if __name__ == "__main__":
    kwdchoice()


@snoop
def kwd_lst():
    """
    Collects a list of all tags in the database.
    """
    query = "SELECT t1 FROM cli_apps UNION SELECT t2 FROM cli_apps UNION SELECT t3 FROM cli_apps UNION SELECT t4 FROM cli_apps"
    clquery = dbdata(query, "fetch")
    klst = [i[0] for i in clquery]

    return klst


if __name__ == "__main__":
    kwd_lst()


@snoop
def showks():
    """
    Calls 'kwd_lst' tag list and presents it to
    the user through 'fzf'. If the user makes
    any selections, creates a pickle file
    with the results.
    """
    klst = kwd_lst()
    print("Choose the tags that interest you. If any.")
    sleep(0.5)
    newtgs = fzf.prompt(
        klst,
        '--border bold --border-label="╢Choose Some Tags!╟" --border-label-pos bottom',
    )
    if newtgs != []:
        with open("keywords.bin", "wb") as f:
            pickle.dump(newtgs, f)


if __name__ == "__main__":
    showks()


@snoop
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
        kwds_expression()
        get_kwds()
        os.remove("kquery.bin")
        os.remove("keywords.bin")
    else:
        kwdchoice()
        with open("chc.bin", "rb") as f:
            choice = pickle.load(f)

        if choice == "y":
            kwd_lst()
            showks()
            kwds_expression()
            get_kwds()
            os.remove("kquery.bin")
            os.remove("chc.bin")
            os.remove("keywords.bin")
            os.remove("chc.bin")
        else:
            os.remove("chc.bin")


if __name__ == "__main__":
    kwd_mngmnt()
