"""
We'll use yay's package information system
to get information on installed packages.
"""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from mysql.connector import Error, connect

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
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
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT DISTINCT name FROM cli_apps"
        cur.execute(query)
        record = cur.fetchall()
        records = [i for t in record for i in t]
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    new_lst = [v for v in clean if v not in records]

    for name in new_lst:
        cmd = f"yay -Si {name} > package_files/{name}.txt"
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    query_builder()
