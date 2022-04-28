"""
It's through this that updates
will be possible.
"""
import subprocess
import time

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
def update():
    """
    The updates are made by
    stating a column and an id.
    With that it's possible
    to direct a user to the
    right content.
    """

    coluna = input(click.style(" Column? » ", fg="bright_green", bold=True))
    ident = input(click.style(" ID? » ", fg="bright_green", bold=True))
    print(click.style(" Write your update", fg="bright_green", bold=True))
    time.sleep(0.3)
    update = click.edit()

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = " UPDATE cli_apps SET " + coluna + " = '" + update + "' WHERE id = " + ident
        print(query)
        cur.execute(query)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    update()
