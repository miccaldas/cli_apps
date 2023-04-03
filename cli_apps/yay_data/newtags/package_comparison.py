"""
We'll compare the list created by Pacman of installed packages with the
databases' list of packages. We'll see what is already in the database
or not. We'll deal with both differently.
"""
import os
import pickle

import mysql.connector
import snoop
from mysql.connector import Error, connect
from snoop import pp

# import subprocess


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


@snoop
def package_lists():
    """"""
    with open("packages.txt", "r") as f:
        pacman_lst = f.readlines()

    result = []
    templst = []

    for i in pacman_lst:
        if i == "\n":
            templst.append(i)
            result.append(templst)
            templst = []
        else:
            templst.append(i)
    result.append(templst)

    no_empties = [i for i in result if i != []]

    with open("paclst.bin", "wb") as g:
        pickle.dump(no_empties, g)

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="cli_apps"
        )
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


# if __name__ == "__main__":
#     package_lists()


@snoop
def column_lst():
    """"""
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


# if __name__ == "__main__":
#     column_lst()


@snoop
def package_comparison():
    """"""
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


# if __name__ == "__main__":
#     package_comparison()


@snoop
def upload_new():
    """"""
    with open("newentries.bin", "rb") as f:
        newentries = pickle.load(f)

    try:
        for entry in newentries:
            name = entry[0]
            presentation = entry[1]
            url = entry[2]
            t1 = entry[0]
            answers = [name, presentation, url, t1]
            conn = connect(
                host="localhost", user="mic", password="xxxx", database="cli_apps"
            )
            cur = conn.cursor()
            query = "INSERT INTO cli_apps (name, presentation, url, t1) VALUES (%s, %s, %s, %s)"
            try:
                cur.execute(query, answers)
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
