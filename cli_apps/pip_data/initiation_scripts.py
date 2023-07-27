"""
These are the initial steps in the update process.
Its name *_scripts* came from the fact that, originally,
these tasks were done by bash scripts. But, as I grew more
confident using the unbelievably cumbersome Python's regex,
I finally was able to have all of code in Python.\n
The first command asks pip for a list, and the second
removes everything except the name.
"""
import os
import pickle
import re
import subprocess

from db import dbdata

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def db_data():
    """
    Takes a list of all names in the db.
    """
    query = "SELECT name FROM cli_apps"
    lst = dbdata(query, "fetch")
    lt = [i for sub in lst for i in sub]
    with open("lists/old_names_linux.bin", "wb") as f:
        pickle.dump(lt, f)


if __name__ == "__main__":
    db_data()


# @snoop
def initiation_scripts():
    """
    We use a *Pip* command to get the list of installed packages::

        pip list --format freeze

    Then we create a file with only the packages names, with the help
    of some *Python's* regex.
    """
    cwd = os.getcwd()
    file = f"{cwd}/lists/first_pip.txt"
    cmd = f"pip list --format freeze > '{file}'"
    subprocess.run(cmd, shell=True)

    with open(file, "r") as f:
        file = f.readlines()

    lines = []
    for line in file:
        # Deletes everything after the '==' sign. It's information on version which we don't care here.'
        name = re.sub("==.*$", "", line)
        lines.append(name)

    for o in lines:
        with open(f"{cwd}/lists/names_linux.txt", "a") as f:
            f.write(f"{o}")


if __name__ == "__main__":
    initiation_scripts()
