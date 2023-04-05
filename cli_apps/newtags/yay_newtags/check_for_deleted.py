"""
I have a feeling that there are some entries in the *cli_apps* database, that were already deleted.
To check for this, we'll get a list of all *yay* and *pip* packages installed, and compare it to the
entries in the db. If there's entries in *cli_apps* that are not in the lists, they're deleted packages.
"""
import os
import pickle
import re
import subprocess

import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def clean_lists():
    """
    We'll get the *pip* and *yay* package lists, and clean them
    until we have only the package names. We'll then create a
    list to put them together.
    """

    with open("piplist.txt", "r") as f:
        piplist = f.readlines()

    names = []
    for line in piplist:
        name = re.sub("==(.*$)", "", line)
        names.append(name.strip())

    with open("yaylist.txt", "r") as d:
        yaylst = d.readlines()

    nms = []
    for line in yaylst:
        if line.startswith("Name"):
            nms.append(line[18:].strip())

    allpacks = nms + names
    with open("allpacks.bin", "wb") as t:
        pickle.dump(allpacks, t)


if __name__ == "__main__":
    clean_lists()


@snoop
def db_pack_lst():
    """
    Download a list of all packages in the database.
    """

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT name FROM cli_apps"
        cur.execute(query)
        recs = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    records = [i for t in recs for i in t]

    with open("records.bin", "wb") as f:
        pickle.dump(records, f)


if __name__ == "__main__":
    db_pack_lst()


@snoop
def compare_lsts():
    """
    We'll compare the lists to see if there's something to be erased.
    """

    with open("allpacks.bin", "rb") as f:
        yay_pip_pcks = pickle.load(f)
    yaypip_pcks = [i.strip() for i in yay_pip_pcks]

    with open("records.bin", "rb") as v:
        db_pcks = pickle.load(v)
    dbpcks = [u.strip() for u in db_pcks]

    comparison = [i for i in dbpcks if i not in yaypip_pcks]
    with open("comparison.bin", "wb") as y:
        pickle.dump(comparison, y)


if __name__ == "__main__":
    compare_lsts()


@snoop
def delete_entries():
    """
    We'll delete from the database the entries that we found
    through the *comparison* list.
    """

    with open("comparison.bin", "rb") as f:
        comparison = pickle.load(f)

    try:
        for entry in comparison:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            answers = [entry]
            query = "DELETE FROM cli_apps WHERE name = %s"
            cur.execute(query, answers)
            conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    delete_entries()
