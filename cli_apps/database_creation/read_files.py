"""
Here we'll create a process to iterate through
all finished files, take out their content,
bind to the file name as tuple, to, later,
upload it to a new database.
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
def read_files():
    """
    We are going to the 'finished-files'
    directory, open each file, create a
    tuple with filename and said content,
    and then get it all into a list.
    """

    dir = "/home/mic/python/cli_apps/cli_apps/text_files/finished_files/"
    finished_lst = os.listdir(dir)

    os.chdir(dir)
    flst = []
    fflst = []
    for name in finished_lst:
        with open(name, "r") as f:
            content = str(f.readlines())
            flst.append((name[:-4], str(content)))
    print(flst)
    print(type(flst[0]))
    print(type(flst[0][0]))
    print(type(flst[0][1]))

    for i in flst:
        fflst.append((i[0], i[1][2:-5]))
    print(fflst)

    return fflst


if __name__ == "__main__":
    read_files()
