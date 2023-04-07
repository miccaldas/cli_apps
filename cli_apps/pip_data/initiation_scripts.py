"""
These are the initial steps in the update process.
Its name *_scripts* came from the fact that, originally,
these tasks were done by bash scripts. But, as I grew more
confident using the unbelievably cumbersome Python's regex,
I finally was able to have all of code in Python.\n
The first command ask pip for a list, and the second
removes everything except the name.
"""
import os
import re
import subprocess

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def initiation_scripts():
    """
    We use a *Pip* command to get the lsit of installed packages::

        pip list --format freeze

    Then we create a file with only the packages names, with the help
    of some *Python's* regex.
    """

    file = "/home/mic/python/cli_apps/cli_apps/pip_data/lists/first_pip.txt"
    cmd = f"pip list --format freeze > '{file}'"
    subprocess.run(cmd, shell=True)

    with open(file, "r") as f:
        file = f.readlines()

    lines = []
    for line in file:
        name = re.sub("==.*$", "", line)
        lines.append(name)

    for o in lines:
        with open(
            "/home/mic/python/cli_apps/cli_apps/pip_data/lists/names_linux.txt", "a"
        ) as f:
            f.write(f"{o}")


if __name__ == "__main__":
    initiation_scripts()
