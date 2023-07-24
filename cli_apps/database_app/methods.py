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
    allinfo = [
        (a, b, c, d.strftime("%d/%m/%Y"), e, f, g, h, i)
        for a, b, c, d, e, f, g, h, i in allinf
    ]

    with open("allinfo.bin", "wb") as f:
        pickle.dump(allinfo, f)


if __name__ == "__main__":
    aggregate_info()


@snoop
def yay_info(srch):
    """
    Module to extract information on
    packages from 'yay'. There are
    several types of input that come
    to this function, if it comes
    from fzf, its a string that needs
    to be evaluated to a list, if it
    comes from 'required_by', it could
    a string or a list of strings. I
    expect the complexity will only
    grow, as we add other services
    using this function.
    """

    if type(srch) == list:
        # 'srch' comes from 'srch_allinfo', will need to evaluate the
        # output, as 'fzf' presents a list as a string. To id it,
        # 'srch_allinfo' adds, at the end of 'srch', the string 'ai'.
        # This way we'll know we can't process it without evaluating it.
        if srch[-1] == "ai":
            # In this case, 'srch' will be two member tuple; the first, a
            # string with information, the second, a code to identify its
            # provenance. We only need the first.
            for i in srch[0]:
                selection = eval(i)
                cmd = f"yay -Qi {selection[1]} > data_files/{selection[1]}_yay"
                subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)
                # As the error the comand generates is a shell command, python
                # has no notion of an error. So, to check if the 'yay' command
                # ended successfully, we'll look at the size of supposdly created
                # file. If it's 0, it means that it errored out.
                stat = os.stat(f"data_files/{selection[1]}_yay")
                if stat.st_size == 0:
                    cmd1 = (
                        f"yay -Qi python-{selection[1]} > data_files/{selection[1]}_yay"
                    )
                    subprocess.run(cmd1, cwd=f"{os.getcwd()}", shell=True)
        else:
            # If it's a list and doesn't have an 'ai' entry, it didn't cpme 'fzx'
            # and it doesn't need to be evaluated.
            for s in srch:
                cmd2 = f"yay -Qi {s[1]} > required_files/{s[1]}"
                subprocess.run(cmd2, cwd=f"{os.getcwd()}", shell=True)
    else:
        # We're assuming it comes from 'request_by' and only has one item to search.
        for t in srch:
            cmd3 = f"yay -Qi {t[1]} > required_files/{s[1]}"
            subprocess.run(cmd3, cwd=f"{os.getcwd()}", shell=True)


if __name__ == "__main__":
    yay_info()


@snoop
def pip_info(srch):
    """
    Module to extract information on
    packages from 'pip'.
    """

    if type(srch) == list:
        if srch[-1] == "ai":
            # In this case, 'srch' will be two member tuple; the first, a
            # string with information, the second, a code to identify its
            # provenance. We only need the first.
            for i in srch[0]:
                selection = eval()
                if selection[1].startswith("python-"):
                    select = selection[1][5:]
                    come = "pip show select"
                    subprocess.run(come, cwd=f"{os.getcwd()}", shell=True)
                cmd = f"pip show {selection[1]} > data_files/{selection[1]}_pip"
                subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)
        else:
            for s in srch:
                cmd1 = f"pip show {s[1]}"
                subprocess.run(cmd1, cwd=f"{os.getcwd()}", shell=True)
    if type(srch) == str:
        cmd2 = f"pip show {srch} > required_files/{srch}_pip"
        subprocess.run(cmd2, cwd=f"{os.getcwd()}", shell=True)


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

    # srch = fzf.prompt(allinfo)
    sr = fzf.prompt(allinfo)
    srch = (sr, "ai")
    print(srch)
    # pip_info(srch)
    yay_info(srch)


if __name__ == "__main__":
    srch_allinfo()
