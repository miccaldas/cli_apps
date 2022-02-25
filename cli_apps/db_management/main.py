"""
Main module, the one that
calls all the other
modules.
"""
from __future__ import unicode_literals

import subprocess
import sys

import isort  # noqa: F401
import questionary
import snoop
from add import add
from delete import delete
from loguru import logger
from search import search
from see import see
from update import update

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @logger.catch
# @snoop
def main():
    """
    It's basically an interface
    for the user, that given
    the input, will pass along
    the request to the other
    functions.
    """
    resposta = questionary.select(
        "What do you want to do?", choices=["Add a Package", "Search for a Package", "See Packages", "Update a Package", "Delete a Package", "Exit"]
    ).ask()

    if resposta == "Add a Package":
        add()
    if resposta == "Search for a Package":
        search()
    if resposta == "See Packages":
        see()
    if resposta == "Update a Package":
        update()
    if resposta == "Delete a Package":
        delete()
    if resposta == "Exit":
        sys.exit()


if __name__ == "__main__":
    main()
