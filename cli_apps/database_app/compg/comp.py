"""
Module Docstring
"""
# import os
# import subprocess
import pickle

import snoop
from db import dbdata
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def comp():
    """
    Took the data of all programs registered in PATH
    with 'compgen'. Subtracted the ones that are in
    'cli_apps' and created a pickle file with the
    results.
    """
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


# @snoop
def zsh_bindings():
    """
    'new' is full of small programs that are
    nothing but zsh key bindings. I'll send
    it to its own list.
    """
    with open("new.bin", "rb") as f:
        new = pickle.load(f)

    zsh_bindings = [
        i
        for i in new
        if i.startswith("zsh_autosuggest") or i.startswith("zsh_highlight")
    ]
    with open("zsh_bindings.bin", "wb") as g:
        pickle.dump(zsh_bindings, g)

    nnew = [i for i in new if i not in zsh_bindings]
    with open("nnew.bin", "wb") as h:
        pickle.dump(nnew, h)


@snoop
def manlst():
    """
    Creation of list of man pages
    that we can use with the compgen
    list.
    """
    with open("manlst.txt", "r") as f:
        ml = f.readlines()

    mnl = [i.split(" ")[0] for i in ml]

    with open("nnew.bin", "rb") as g:
        new = pickle.load(g)

    mansplain = [i for i in new if i in mnl]
    print(mansplain)
    print(len(mansplain))


if __name__ == "__main__":
    #     comp()
    # zsh_bindings()
    manlst()
