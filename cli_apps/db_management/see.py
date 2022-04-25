"""
Module that gives access to the
whole of the dataabse.
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
def see():
    """
    Call the db and
    ask it to dump
    its content.
    """

    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = """ SELECT * FROM cli_apps ORDER BY rand()"""
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(click.style(" [*] ID » ", fg="bright_green", bold=True), click.style(str(row[0]), fg="bright_white", bold=True))
            print(click.style(" [*] NAME » ", fg="bright_green", bold=True), click.style(str(row[1]), fg="bright_white", bold=True))
            print(click.style(" [*] PRESENTATION » ", fg="bright_green", bold=True), click.style(str(row[2]), fg="bright_white", bold=True))
            print(click.style(" [*] URL ", fg="bright_green", bold=True), click.style(str(row[4]), fg="bright_white", bold=True))
            print(click.style(" [*] TIME » ", fg="bright_green", bold=True), click.style(str(row[3]), fg="bright_white", bold=True))
            print(click.style(" [*] TAG » ", fg="bright_green", bold=True), click.style(str(row[5]), fg="bright_white", bold=True))
            print(click.style(" ------------------------------------------------------------ ", fg="bright_white", bold=True))
            print("\n")
            conn.close()
    except Error as e:
        print("Error while connecting to db", e)


if __name__ == "__main__":
    see()
