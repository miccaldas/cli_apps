"""
Since the shell scripts couldn't clean everything,
we'll use this module to clean what is still to
clean of the original results.csv.
"""
import glob
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
def post_cleansh():
    """
    We'll delete most of the transitional files but
    we'll keep each last iteration, for further
    operations. It will be a mix of python and shell
    methods.
    """

    cwd = os.getcwd()
    dir = f"{cwd}/text_files/transitional_files/"
    file0 = f"{dir}*_trans0.txt"
    files0 = glob.glob(file0)
    print(files0)


if __name__ == "__main__":
    post_cleansh()
