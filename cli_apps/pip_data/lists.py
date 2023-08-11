"""
Gets lists of package names in the db and another of pip
installed packages. Compares them to see if the latter
has packages not in included in the former. If it has,
builds a list with the names of these packages, searches
for information on them with 'pip show', selects only the
'name', 'summary' and 'home-page' lines of each entry. To
use as sources for the 'name', presentation' and 'url' db
columns.
"""
import os
import pickle

from db import dbdata

# import snoop


# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def db_data() -> None:
    """
    Takes a list of all names in the db.
    """
    query = "SELECT name FROM cli_apps"
    lst: list[tuple[str]] = dbdata(query, "fetch", answers=None)
    lt: list[str] = [i for sub in lst for i in sub]
    with open("lists/db_names.bin", "wb") as f:
        pickle.dump(lt, f)


if __name__ == "__main__":
    db_data()


# @snoop
def pip_list() -> None:
    """
    We use a *Pip* command to get the list of installed packages::

        pip list

    Then we create a file with only the packages names, with the help
    of some *Python's* regex.
    """
    cwd = "/home/mic/python/cli_apps/cli_apps/pip_data"
    fpip = f"{cwd}/lists/first_pip.txt"

    os.system(f"python -m pip list > '{fpip}'")

    with open(fpip, "r") as f:
        fil: list[str] = f.readlines()

    fil.pop(0)
    fl: list = [i.split(" ")[0] for i in fil]
    fl.pop(0)
    file: list = list(set(fl))

    with open(f"{cwd}/lists/pip_names.bin", "wb") as f:
        pickle.dump(file, f)


if __name__ == "__main__":
    pip_list()


# @snoop
def new_entries() -> str:
    """
    We'll see if *pip_names.bin has
    any packages present in *db_names.bin*.
    """
    with open("lists/db_names.bin", "rb") as f:
        db: list[str] = pickle.load(f)
    with open("lists/pip_names.bin", "rb") as g:
        pip: list[str] = pickle.load(g)

    # The command 'not in db', was giving a lot of false positives. We use four  possible ways of writing a package.
    nw: list[str] = [i for i in pip if i not in db and i.lower() not in db and f"python-{i}" not in db and f"python-{i.lower()}" not in db]

    # Even with four possible wordings, there are packages that are in the db, but python
    # says they're not. As they'll probably reccur everytime we run this, I made a list
    # of them and we'll remove them this way.
    fp = [
        "snoop",
        "Plost",
        "Jinja2",
        "ranger-fm",
        "streamlit",
        "torch",
        "pycairo",
        "pwquality",
        "CT3",
    ]
    for r in fp:
        if r in nw:
            nw.remove(r)

    if nw != []:
        with open("lists/newentries.bin", "wb") as f:
            pickle.dump(nw, f)
        return "y"
    else:
        return "n"


if __name__ == "__main__":
    new_entries()


# @snoop
def pip_show() -> None:
    """
    Uses the 'pip show' command to gather data
    on the packages in 'newnetries.bin', cleans
    the results and creates a file with the
    results.
    """
    with open("lists/newentries.bin", "rb") as f:
        ne: list[str] = pickle.load(f)

    for n in ne:
        os.system(f"python -m pip show {n} >> packages.txt")
        os.system("echo ' ' >> packages.txt")


if __name__ == "__main__":
    pip_show()


# @snoop
def txt_cleaner() -> None:
    """
    Text cleaner for 'packages.txt'.
    Divides the text output in packages,
    selects 'name', 'summary' and 'home-page'
    as entries for the db. Creates a file with
    the results.
    """
    pth = "/home/mic/python/cli_apps/cli_apps/pip_data/"
    with open(f"{pth}/packages.txt", "r") as f:
        reader: list[str] = f.readlines()

    # Divides the text output in sublists.
    lst: list[list[str]] = []
    temp: list[str] = []
    for line in reader:
        # Notice that because I created a gap between package information
        # on the text file with "' '", that line, for python looks like a
        # space and breakline symbol. Don't just put a breakline symbol as
        # my dumb self did, and was debugging for a long time.
        if line == " \n":
            temp.append(line)
            lst.append(temp)
            temp = []
        else:
            temp.append(line)

    # Creates a new list with just the 'name', 'summary' and 'home-page' values,
    # without their prefixes and linebreaks.
    cln: list[list[str]] = [[y[0][6:].strip(), y[2][9:].strip(), y[3][11:].strip()] for y in lst]

    with open("/home/mic/python/cli_apps/cli_apps/pip_data/nospaces.bin", "wb") as t:
        pickle.dump(cln, t)


if __name__ == "__main__":
    txt_cleaner()
