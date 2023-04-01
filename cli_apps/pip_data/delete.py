"""
Clears the package of unnecessary
files. We keep 'names_linux.txt',
because it's important to compare
each draw, and only handle what is
new.
"""
import os
import subprocess

# import snoop


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


#@snoop
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
