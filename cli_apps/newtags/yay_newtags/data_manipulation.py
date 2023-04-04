"""
We'll compare the list created by Pacman of installed packages with the
databases' list of packages. We'll see what is already in the database
or not. We'll deal with both differently.
"""
import os
import pickle
import subprocess

import mysql.connector
import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def package_lists():
    """
    Here we create two lists:\n
    1. List of lists with the information from each package in a sublist.\n
    Taken from the command::

           sudo pacman -Qi

    2. List of all db entries that haven't got keyword values.\n
    Both lists are pickled for future use.
    """
    with open("packages.txt", "r") as f:
        pacman_lst = f.readlines()

    result = []
    templst = []
    # In order to turn the single list with all the results jumbled up from
    # 'pacman', we'll break it in sublists at the ocurrence of line with a
    # line break only. That's where the entries separate. We create a list
    # 'templst' to get the sublist results, and use the 'result' list to
    # append it. Everytime 'templst' finds a lone linebreak, it becomes an
    # empty list, and the cicle begins again.
    for i in pacman_lst:
        if i == "\n":
            templst.append(i)
            result.append(templst)
            templst = []
        else:
            templst.append(i)

    with open("paclst.bin", "wb") as g:
        pickle.dump(result, g)

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT name FROM cli_apps WHERE t2 IS NULL"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    recs = [r for g in records for r in g]
    with open("recs.bin", "wb") as y:
        pickle.dump(recs, y)


if __name__ == "__main__":
    package_lists()


@snoop
def column_lst():
    """
    We clean 'paclst' of everything that's not to be used in 'cli_apps' columns.\n
    We keep only:\n
    1.  Name.\n
    2.  Description.\n
    3.  URL.\n
    """
    with open("paclst.bin", "rb") as f:
        paclst = pickle.load(f)

    columns = []
    entries = []
    for package in paclst:
        for item in package:
            if item.startswith("Name"):
                entries.append(item.strip())
            if item.startswith("Description "):
                entries.append(item.strip())
            if item.startswith("URL "):
                entries.append(item.strip())
        columns.append(entries)
        entries = []

    with open("columns.bin", "wb") as d:
        pickle.dump(columns, d)


if __name__ == "__main__":
    column_lst()


@snoop
def package_comparison():
    """
    As we have new packages to upload, before worrying with keyword values,
    we'll make a list of what packages *Pacman* discovered that are not in
    the database.
    We clean the title prefixes on each line of columns and make pickle files
    of two groups:\n
    1. Packages not in database.
    2. Packages already in the database.
    """
    with open("recs.bin", "rb") as f:
        recs = pickle.load(f)

    with open("columns.bin", "rb") as o:
        columns = pickle.load(o)

    newpacks = [i for i in columns if i[0][18:] not in recs]
    oldpacks = [b for b in columns if b[0][18:] in recs]

    newentries = [(a[18:], b[18:], c[18:]) for a, b, c in newpacks]
    with open("newentries.bin", "wb") as g:
        pickle.dump(newentries, g)

    oldentries = [(a[18:], b[18:], c[18:]) for a, b, c in oldpacks]
    with open("oldentries.bin", "wb") as u:
        pickle.dump(oldentries, u)


if __name__ == "__main__":
    package_comparison()


@snoop
def upload_new():
    """
    Uploading the new packages to *cli_apps*.
    """
    with open("newentries.bin", "rb") as f:
        newentries = pickle.load(f)

    try:
        for entry in newentries:
            name = entry[0]
            presentation = entry[1]
            url = entry[2]
            t1 = entry[0]
            answers = [name, presentation, url, t1]
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "INSERT INTO cli_apps (name, presentation, url, t1) VALUES (%s, %s, %s, %s)"
            try:
                cur.execute(query, answers)
            # MySQL would stop when it had a repeated entry to upload. With this block he doesn't
            # uploads it, as we don't want that, but doesn't stop and continues processing the rest
            # of the list.
            except mysql.connector.errors.IntegrityError:
                pass
            conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    upload_new()


@snoop
def adding_lists():
    """
    There's entries in *cli_apps* without keyword values.
    We, on the other hand, have a list of entries, some new,
    some old, that'll need to have keywords defined.
    Let's join these lists, sort out repeats, and work
    from there.
    """

    with open("columns.bin", "rb") as f:
        columns = pickle.load(f)

    cleancols = [(a[18:], c[18:]) for a, b, c in columns]

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT name, url FROM cli_apps WHERE t2 = 'NA'"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    allcols = cleancols + records
    # Here we turn 'allcols' to a dictionary, 'dict.fromkeys(allcols)', which eliminates
    # duplicates. Then we convert it back to list; 'sortedcols = list(...)'.
    sortedcols = list(dict.fromkeys(allcols))
    with open("sortedcols.bin", "wb") as m:
        pickle.dump(sortedcols, m)


if __name__ == "__main__":
    adding_lists()


@snoop
def cleaning_list():
    """
    There were columns, still, with linebreak symbols. Probably
    taken from the db. We clean them, delete an entry that is
    only one letter, and pickle it.
    """
    cwd = os.getcwd()
    projects = f"{cwd}/projects"

    with open("sortedcols.bin", "rb") as f:
        columns = pickle.load(f)

    cols = []
    item = []
    for col in columns:
        for val in col:
            nm = val.strip()
            item.append(nm)
        cols.append(item)
        item = []

    smallcols = [(a, b) for a, b in cols if len(a) > 1]
    setcols = list(dict.fromkeys(smallcols))
    with open("setcols.bin", "wb") as t:
        pickle.dump(setcols, t)


if __name__ == "__main__":
    cleaning_list()


@snoop
def name_change():
    """
    Some of these names have dashes and dots on them, and Scrapy
    doesn't accept them on its spider's/project's names.
    To comply, but not forget original name, we add a chenged
    version, with underline, as first element of the tuple.\n
    .. NOTE::
        This change turned out to be useless, since we decided to
        create just one project, with all the spiders inside it.
        I leave it here for documentation purposes.
    """
    with open("setcols.bin", "rb") as f:
        setcols = pickle.load(f)

    dotname = [(h.replace(".", "_"), h, d) for h, d in setcols]
    newname = [(n.replace("-", "_"), i, o) for n, i, o in dotname]
    with open("newname.bin", "wb") as v:
        pickle.dump(newname, v)


if __name__ == "__main__":
    name_change()


@snoop
def xorg_urls():
    """
    All Xorg packages had as URL, a generic *Freedesktop* site
    url, which won't bring much information. We replace them
    with url's to their *Github* pages.
    """
    with open("newname.bin", "rb") as f:
        newname = pickle.load(f)

    newurls = []
    for entry in newname:
        if entry[2] == "https://xorg.freedesktop.org/":
            if entry[1].startswith("xorg-"):
                newurl = f"https://github.com/freedesktop/{entry[1]}"
            else:
                newurl = f"https://github.com/freedesktop/xorg-{entry[1]}"
            newurls.append((entry[0], entry[1], newurl))
        else:
            newurls.append(entry)

    with open("newurls.bin", "wb") as v:
        pickle.dump(newurls, v)


if __name__ == "__main__":
    xorg_urls()
