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

    ident = input(click.style(" ID to delete? » ", fg="bright_white", bold=True))
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = " DELETE FROM cli_apps WHERE id = " + ident
        cur.execute(query)
        conn.commit()
        print(click.style(f" ID #{ident} was deleted.", fg="bright_green", bold=True))

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    delete()
