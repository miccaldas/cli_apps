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
from loguru import logger
from questionary import Style

from add import add
from delete import delete
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

    custom_style_package = Style(
        [
            ("qmark", "fg:#E4BAD4 bold"),
            ("question", "fg:#F5E8C7 bold"),
            ("answer", "fg:#F4C7AB bold"),
            ("pointer", "fg:#F6D7A7 bold"),
            ("highlighted", "fg:#E0C097 bold"),
            ("selected", "fg:#D3E4CD bold"),
            ("text", "fg:#F8F0DF bold"),
        ]
    )

    resposta = questionary.select(
        "What do you want to do?",
        qmark="[++]",
        pointer="»»",
        use_indicator=True,
        style=custom_style_package,
        choices=["Add a Package", "Search for a Package", "See Packages", "Update a Package", "Delete a Package", "Exit"],
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
