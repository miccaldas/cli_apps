"""
We'll use pip's package information system
to get information on installed packages.
"""
import os
import subprocess

import isort  # noqa: F401
import snoop
from loguru import logger
from snoop import pp

fmt = "{time} - {name} - {level} - {message}"
logger.add("../logs/info.log", level="INFO", format=fmt, backtrace=True, diagnose=True)  # noqa: E501
logger.add("../logs/error.log", level="ERROR", format=fmt, backtrace=True, diagnose=True)  # noqa: E501

subprocess.run(["isort", __file__])


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@logger.catch
@snoop()
def query_builder():
    """
    We'll instantiate the lists
    here, compare it to the old
    name list, and keep only
    new entries. Then we'll pass
    these entries through a
    subprocess command, that will
    link to pip.
    """

    cwd = os.getcwd()
    name_path = f"{cwd}/lists/names_linux.txt"
    old_name_path = f"{cwd}/lists/old_names_linux.txt"

    with open(name_path, "r") as f:
        names = f.readlines()

    with open(old_name_path, "r") as f:
        old_names = f.readlines()

    clean = [i.strip() for i in names]
    print(clean)
    old_clean = [v.strip() for v in old_names]

    for name in clean:
        if pp(name not in old_clean):
            cmd = f"pip show {name} > package_files/{name}.txt"
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    query_builder()
