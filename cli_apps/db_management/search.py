"""
Module that will do the search
in the  dataabse.
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
def search():
    """
    This search is supported by
    MySQL's fulltext search,
    that permits to do syntactic
    queries to the database.
    """

    try:
        busca = input(click.style(" What are you searching for? ", fg="bright_red", bold=True))
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = " SELECT id, name, presentation, url, time FROM cli_apps WHERE MATCH(name, presentation) AGAINST('" + busca + "') "
        cur.execute(query)
        records = cur.fetchall()
        for row in records:
            print(click.style(" [*] ID » ", fg="bright_yellow", bold=True), click.style(str(row[0]), fg="bright_red", bold=True))
            print(click.style(" [*] NAME » ", fg="bright_yellow", bold=True), click.style(str(row[1]), fg="bright_red", bold=True))
            print(click.style(" [*] PRESENTATION » ", fg="bright_yellow", bold=True), click.style(str(row[2]), fg="bright_red", bold=True))
            print(click.style(" [*] URL » ", fg="bright_yellow", bold=True), click.style(str(row[3]), fg="bright_red", bold=True))
            print(click.style(" [*] TIME » ", fg="bright_yellow", bold=True), click.style(str(row[4]), fg="bright_red", bold=True))
            print("\n")
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    search()
