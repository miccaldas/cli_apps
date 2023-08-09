"""
These are the initial steps in the update process.
Its name *_scripts* came from the fact that, originally,
these tasks were done by bash scripts. But, as I grew more
confident using the unbelievably cumbersome Python's regex,
I finally was able to have all of code in Python.\n
The first command asks pip for a list, and the second
removes everything except the name.
"""
import os
import pickle
import re
import subprocess

import snoop

from db import dbdata

# from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def db_data():
    """
    Takes a list of all names in the db.
    """
    query = "SELECT name FROM cli_apps"
    lst = dbdata(query, "fetch")
    lt = [i for sub in lst for i in sub]
    with open("lists/db_names.bin", "wb") as f:
        pickle.dump(lt, f)


# if __name__ == "__main__":
#     db_data()


# @snoop
def initiation_scripts():
    """
    We use a *Pip* command to get the list of installed packages::

        pip list --format freeze

    Then we create a file with only the packages names, with the help
    of some *Python's* regex.
    """
    cwd = "/home/mic/python/cli_apps/cli_apps/pip_data"
    file = f"{cwd}/lists/first_pip.txt"

    os.system(f"sudo pip list > '{file}'")

    with open(file, "r") as f:
        fil = f.readlines()

    fil.pop(0)
    fl = [i.split(" ")[0] for i in fil]
    fl.pop(0)
    file = list(set(fl))

    with open(f"{cwd}/lists/pip_names.bin", "wb") as f:
        pickle.dump(file, f)


# if __name__ == "__main__":
#     initiation_scripts()


@snoop
def new_entries():
    """
    We'll see if *names_linux.bin has
    any packages present in *old_names.bin*.
    """
    with open("lists/db_names.bin", "rb") as f:
        db = pickle.load(f)
    with open("lists/pip_names.bin", "rb") as g:
        pip = pickle.load(g)

    # The command 'nor in db', was giving a lot of false positives. We use two
    # possible ways of writing a package name, to see if helps.
    nw = [i for i in pip if i.lower() not in db and f"python-{i.lower()}" not in db]

    # Even with two possible wordings, there are packages that are in the db, but python
    # says they're not. As they'll probably reccur everytime we run this, I made a list
    # of them and we'll remove them this way.
    fp = [
        "snoop",
        "Plost",
        "Jinja2",
        "ranger-fm",
        "streamlit",
        "torch",
        "pycairo",
        "pwquality",
        "CT3",
    ]
    for r in fp:
        nw.remove(r)

    if nw != []:
        with open("newentries.bin", "wb") as f:
            pickle.dump(nw, f)


if __name__ == "__main__":
    new_entries()
