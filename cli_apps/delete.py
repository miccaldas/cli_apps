"""
Clears the package of unnecessary
files. We keep 'names_linux.txt',
because it's important to compare
each draw, and only handle what is
new.
"""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop
def delete():
    """
    We'll delete all files in the
    'results' and 'package_files'
    folders, and all lists with
    the exception of
    'names_linux.txt'
    """
    cwd = os.getcwd()
    results = f"{cwd}/results"
    packs = f"{cwd}/package_files"

    fldrs = [results, packs]
    for fld in fldrs:
        paths = [os.path.join(fld, file) for file in os.listdir(fld)]
        for path in paths:
            os.remove(path)


if __name__ == "__main__":
    delete()
