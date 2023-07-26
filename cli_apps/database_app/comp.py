"""
Module Docstring
"""
# import os
# import subprocess
import pickle

import snoop
from snoop import pp

from db import dbdata


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def comp():
    """"""
    new = []
    with open("compgen.txt", "r") as f:
        comp = f.readlines()
    cleancomp = [i.strip() for i in comp]
    cl1 = [i[1:] for i in cleancomp if i[0] == "_"]

    query = "SELECT name FROM cli_apps"
    cliapps = dbdata(query, "fetch")
    apps = [i for sub in cliapps for i in sub]

    for c in cl1:
        if c not in apps:
            new.append(c)

    with open("new.bin", "wb") as g:
        pickle.dump(new, g)


if __name__ == "__main__":
    comp()
