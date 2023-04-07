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


# @snoop
def delete():
    """
    We'll delete all files in the *results*,
    'package_files' and *kws* folders, all
    lists, with the exception of
    'names_linux.txt', and all *bin* files.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data"
    results = f"{pip}/results"
    packs = f"{pip}/package_files"
    kws = f"{pip}/tags/kws"

    fldrs = [results, packs, kws]
    for fld in fldrs:
        if os.listdir(fld) != []:
            paths = [os.path.join(fld, file) for file in os.listdir(fld)]
            for path in paths:
                os.remove(path)

    files = os.listdir(f"{pip}/tags")
    for file in files:
        if file.endswith(".bin"):
            os.remove(f"{pip}/tags/{file}")
        if file == "pip_project":
            cmd = f"/usr/bin/trash-put {pip}/tags/pip_project"
            subprocess.run(cmd, shell=True)

    lists = os.listdir(f"{pip}/lists")
    for lst in lists:
        if lst != "names_linux.txt":
            os.remove(f"{pip}/lists/{lst}")


if __name__ == "__main__":
    delete()
