"""
We'll use pip's package information system
to get information on installed packages.
"""
import multiprocessing
import os
import subprocess
from multiprocessing import Pool

# import snoop
from snoop import pp

# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop()
def query_builder(clean):
    """
    We'll instantiate the lists
    here, compare it to the old
    name list, and keep only
    new entries. Then we'll pass
    these entries through a
    subprocess command, that will
    link to pip.
    We'll use multiprocessing to
    speed up the process.
    """

    cwd = os.getcwd()
    old_name_path = f"{cwd}/lists/old_names_linux.txt"

    with open(old_name_path, "r") as f:
        old_names = f.readlines()

    old_clean = [v.strip() for v in old_names]

    if clean not in old_clean:
        cmd = f"pip show {clean} > package_files/{clean}"
        subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    cwd = os.getcwd()
    name_path = f"{cwd}/lists/names_linux.txt"
    with open(name_path, "r") as f:
        names = f.readlines()
    clean = [i.strip() for i in names]
    with Pool() as pool:
        pool.map(query_builder, clean)
