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
    cwd = os.getcwd()
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data"
    results = f"{pip}/results"
    packs = f"{pip}/package_files"
    kws = f"{pip}/tags/kws"

    fldrs = [results, packs, kws]
    for fld in fldrs:
        paths = [os.path.join(fld, file) for file in os.listdir(fld)]
        for path in paths:
            os.remove(path)

    newname = f"{pip}/tags/newname.bin"
    if newname:
        os.remove(newname)
    newurls = f"{pip}/tags/newurls.bin"
    if newurls:
        os.remove(newurls)
    nospaces = f"{pip}/tags/nospaces.bin"
    if nospaces:
        os.remove(nospaces)
    kwdlst = f"{pip}/kwdlst.bin"
    if kwdlst:
        os.remove(kwdlst)
    first_pip = f"{pip}/lists/first_pip.txt"
    if first_pip:
        os.remove(first_pip)
    old_names = f"{pip}/lists/old_names_linux.txt"
    if old_names:
        os.remove(old_names)

    cmd = f"/usr/bin/trash-put {pip}/pip_project"
    subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    delete()
