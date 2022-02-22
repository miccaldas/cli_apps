"""
This module will take care of any uploading to
the db, through this app.
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
def add():
    """
    We'll create a mysql connection and
    upload to the db.
    """

    name = input(click.style(" ++ Name? ++ ", fg="bright_yellow", bold=True))
    presentation = input(click.style(" ++ Presentation? ++ ", fg="bright_yellow", bold=True))
    url = input(click.style(" ++ URL? ++ ", fg="bright_yellow", bold=True))

    answers = [name, presentation, url]

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "INSERT INTO bkmks (name, presentation, url) VALUES (%s, %s, %s)"
        cur.execute(query, answers)
        conn.commit()

    except Error as e:
        print("Error while connecting to db", e)
    finally:
        conn.close()


if __name__ == "__main__":
    add()
