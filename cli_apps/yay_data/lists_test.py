"""
Houses a class created so I can write location information just once.
"""
import os
import pickle
import re
import subprocess

import snoop
from mysql.connector import Error, connect
from snoop import pp

from db import dbdata


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

# Locations
yay = "/home/mic/python/cli_apps/cli_apps/yay_data/"
lists = f"{yay}lists/"


# @snoop
def yay_lst():
    """
    Sources and stores in a file, all *Arch* installed packages::

        yay -Qi > {ists}/yay_lst.txt
    """
    os.system(f"yay -Qi > {lists}/yay_lst.txt")


if __name__ == "__main__":
    yay_lst()


# @snoop
def db_lst():
    """
    Sources, cleans and stores in a file, list of names of packages in the database.\n
    .. code-block:: sql

        SELECT name FROM cli_apps
    """
    query = "SELECT name FROM cli_apps"
    recs = dbdata(query, "fetch")

    records = [h for j in recs for h in j]
    with open(f"{lists}/dblst.bin", "wb") as f:
        pickle.dump(records, f)


if __name__ == "__main__":
    yay_lst()


# @snoop
def yay_names(self):
    """
    Cleans and compares the lists of *Arch* packages and
    the list packages in the database. Whatever is on the
    first list but not on the second is put on a list to
    get imported. Does the following operations:

        1. Breaks the *Arch* list in sublists, each with
        information on each package.\n
        2. Strips lines of linebreaks and deletes empty
        lines.\n
        3. Creates a list of tuples with information on:
            3.1. Name.\n
            3.2. Description.\n
            3.3. URL.
        4. Strips away the line prefix with the title.
        5. Creates list of *Arch* packages not in the db.
        6. Stores it in a file.
    """
    with open(f"{self.lists}/dblst.bin", "rb") as f:
        dblst = pickle.load(f)
    with open(f"{self.lists}/yay_lst.txt", "r") as v:
        yay_lst = v.readlines()
    yay_tups = []
    yaytemp = []
    # Separates 'yay_lst' into sublists. So you isolate each entry.
    for y in yay_lst:
        if y == "\n":
            yaytemp.append(y)
            yay_tups.append(yaytemp)
            yaytemp = []
        else:
            yaytemp.append(y)

    yayclean = []
    cleantemp = []
    # Separates 'yay_tups' into sublists.
    for t in yay_tups:
        for v in t:
            if v != "\n":
                if v.startswith("Validated By    : "):
                    nt = v.strip()
                    cleantemp.append(nt)
                    yayclean.append(cleantemp)
                    cleantemp = []
                else:
                    cleantemp.append(v.strip())

    yayvals = [(t[0], t[2], t[4]) for t in yayclean]
    yaylst = [(a[18:], b[18:], c[18:]) for a, b, c in yayvals]
    newnames = [i for i in yaylst if i[0] not in dblst]

    if newnames != []:
        with open("newnames.bin", "wb") as w:
            pickle.dump(newnames, w)
    else:
        return "n"
