"""
Module to do the preparatory work before inserting
the 'compgen's' information on 'cli_apps. We'll
need to see what is already there, and what is so
unimportant that we'll ignore.
Compgen, I understood just now, it's only a list of
apps in the /usr/bin folder.
"""
import os
import pickle

# import snoop
from cli_apps.database_app.db import dbdata
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def cleaning():
    """
    We get rid of linebreaks and names with forward dashes.
    """
    with open("lists/compgen.txt", "r") as f:
        cg = f.readlines()

    cleancg = [i.strip() for i in cg]
    cleaner = []
    for c in cleancg:
        cleaner.append(c)
        if c.startswith("_"):
            cleaner.append(c[1:])

    with open("cleaner.bin", "wb") as f:
        pickle.dump(cleaner, f)


# @snoop
def db_comparison():
    """
    We compare it with the 'cli_apps' db
    and delete what's already in there.
    """
    with open("cleaner.bin", "rb") as f:
        cleaner = pickle.load(f)

    query = "SELECT name FROM cli_apps ORDER BY id DESC"
    dbnames = dbdata(query, "fetch")
    cleannames = [i for sub in dbnames for i in sub]

    notindb = [i for i in cleaner if i not in cleannames]

    with open("lists/notindb.db", "wb") as g:
        pickle.dump(notindb, g)

    os.remove("cleaner.bin")


# @snoop
def mansplain():
    """
    We'll take out the apps that have man pages
    in the system. It's much more simpler to
    convert it to a file and go from therem than
    having to create a spider to retrieve the data
    we have in-house.
    """
    with open("lists/notindb.bin", "rb") as f:
        nodb = pickle.load(f)

    with open("lists/man_pages_lst.txt", "r") as g:
        mn = g.readlines()

    man = [i.strip() for i in mn]

    short_man = []
    for line in man:
        nm = line.split(" ")[0]
        short_man.append(nm)

    noman = [i for i in nodb if i not in short_man]

    with open("lists/noman.bin", "wb") as g:
        pickle.dump(noman, g)

    print(len(noman))


if __name__ == "__main__":
    # cleaning()
    # db_comparison()
    mansplain()
