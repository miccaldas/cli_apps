"""
We'll use yay's package information system
to get information on installed packages.
"""
import os
import subprocess

#import snoop
from mysql.connector import Error, connect


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def query_builder():
    """
    We'll open the list of packages installled
    by pacman and the AUR and compare it to the
    list of package names already in the db. We
    take into account only the new entries, and
    create the the corresponding package files.
    """

    with open("yay_lst.txt", "r") as f:
        names = f.readlines()

    clean = [i.strip() for i in names]
    print(f"clean is {clean}")

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="cli_apps"
        )
        cur = conn.cursor()
        query = "SELECT DISTINCT name FROM cli_apps"
        cur.execute(query)
        record = cur.fetchall()
        records = [i for t in record for i in t]
    except Error as e:
        err_msg = "Error while connecting to db", e
        print("Error while connecting to db", e)
        if err_msg:
            return query, e
    finally:
        if conn:
            conn.close()

        return query

    new_lst = [v for v in clean if v not in records]

    for name in new_lst:
        cmd = f"yay -Si {name} > package_files/{name}.txt"
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    query_builder()
