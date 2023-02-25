"""
Module to delete entries from
the database.
"""
import subprocess

import click
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


# @logger.catch
# @snoop
def delete():
    """
    As usual, connects to
    db, makes sql query,
    deletes object.
    Deletion is done through
    the row id value.
    """

    ident = input("ID to delete? ")

    # List declared here to avoid errors about being declared before assignment.
    split_lst = []
    if "," in ident:
        query = f"DELETE FROM notes WHERE id IN ({ident})"
    if "-" in ident:
        if " - " in ident:
            answers = ident.replace(" ", "")
            split_lst = answers.split("-")
        else:
            split_lst = ident.split("-")
        query = (
            f"DELETE FROM notes WHERE id BETWEEN {split_lst[0]} AND {split_lst[1]}"
        )
    if "," not in ident and "-" not in ident:
        query = f"DELETE FROM notes WHERE id = '{ident}'"

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query
        cur.execute(query)
        conn.commit()
        conn.close()
    except Error as e:
        err_msg = "Error while connecting to db", e
        print("Error while connecting to db", e)
        if err_msg:
            return query, err_msg

    return query


if __name__ == "__main__":
    delete()
