"""
Houses several methods to be used in building other modules.
"""
import os
import pickle
import subprocess
from datetime import datetime

import snoop
from blessed import Terminal
from pyfzf.pyfzf import FzfPrompt
from snoop import pp

from db import dbdata


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def checkinfo():
    """
    We'll check what 'bin' files there are,
    and make a list of their names.
    """
    filelst = os.listdir(os.getcwd())
    srch_results = ["qlst.bin", "klst.bin", "ilst.bin", "nlst.bin"]
    results = [i for i in srch_results if i in filelst]

    return results


if __name__ == "__main__":
    checkinfo()


@snoop
def aggregate_info():
    """
    Collects and merges file contents produced by 'search'.
    """
    fls = checkinfo()
    allinf = []

    for f in fls:
        with open(f, "rb") as fl:
            partial = pickle.load(fl)
            if partial != [] and partial != "":
                for i in partial:
                    # This code allows to merge to an existing list,
                    # elements of another.
                    allinf += [i]
    allinfo = [(a, b, c, d.strftime("%d/%m/%Y"), e, f, g, h, i) for a, b, c, d, e, f, g, h, i in allinf]

    with open("allinfo.bin", "wb") as f:
        pickle.dump(allinfo, f)


if __name__ == "__main__":
    aggregate_info()


@snoop
def yay_info(srch):
    """
    Module to extract information on
    packages from 'yay'.
    """
    for i in srch:
        selection = eval(i)
        if selection[1].startswith("python-"):
            cmd = f"yay -Qi {selection[1]} > data_files/{selection[1]}_yay"
            subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)
            # As the error the comand generates is a shell command, python
            # has no notion of an error. So, to check if the 'yay' command
            # ended successfully, we'll look at the size of supposdly created
            # file. If it's 0, it means that it errored out.
            stat = os.stat(f"data_files/{selection[1]}_yay")
            if stat.st_size == 0:
                cmd1 = f"yay -Qi python-{selection[1]} > data_files/{selection[1]}_yay"
                subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)
        else:
            cmd2 = f"yay -Qi python-{selection[1]} > data_files/{selection[1]}_yay"
            subprocess.run(cmd2, cwd=f"{os.getcwd()}", shell=True)


if __name__ == "__main__":
    yay_info()


@snoop
def pip_info(srch):
    """
    Module to extract information on
    packages from 'pip'.
    """
    for i in srch:
        selection = eval(i)
        cmd = f"pip show {selection[1]} > data_files/{selection[1]}_pip"
        subprocess.run(cmd, cwd=os.getcwd(), shell=True)


if __name__ == "__main__":
    pip_info()


@snoop
def srch_allinfo():
    """
    Searches 'allinfo' with fzf and, if needed,
    collects user selections.
    """
    fzf = FzfPrompt()

    with open("allinfo.bin", "rb") as f:
        allinfo = pickle.load(f)

    srch = fzf.prompt(allinfo)

    pip_info(srch)
    yay_info(srch)


if __name__ == "__main__":
    srch_allinfo()
