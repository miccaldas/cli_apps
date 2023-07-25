"""
Houses several methods to be used in building other modules.
"""
import os
import os.path
import pickle
import subprocess
from datetime import datetime

import snoop
from click import style
from pyfzf.pyfzf import FzfPrompt
from rich import print
from rich.console import Console
from snoop import pp

from db import dbdata
from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def input_decision(prompt):
    """
    Template for inputs, asking the user
    for a decision.
    """
    console = Console()

    print("\n")
    dec = input(
        style(
            f"          {prompt} ",
            fg=(160, 196, 157),
            bold=True,
        )
    )
    print("\n")

    return dec


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
def subcall(shellcmd, flnm, fldr, flnmid):
    """
    Makes 'subprocess' calls for 'yay_info'
    and 'pip_info'. To simplify the code.
    """
    cmd = f"{shellcmd} {flnm} > {fldr}/{flnm}{flnmid}"
    subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)


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
    shellcmd = "yay -Qi"

    # If 'srch' comes from 'srch_allinfo', will need to evaluate the
    # output, as 'fzf' presents a list as a string. To id it,
    # 'srch_allinfo' adds, at the end of 'srch', the string 'ai'.
    # This way we'll know we can't process it without evaluating it.
    if srch[-1] == "ai":
        fldr = "data_files"
        # In this case, 'srch' will be two member tuple; the first, a
        # string with information, the second, a code to identify its
        # provenance. We only need the first.
        for i in srch[0]:
            selection = eval(i)
            if selection[1].startswith("python-"):
                flnm = f"{selection[1]}"
            else:
                flnm = f"python-{selection[1]}"
            flnmid = "_yay"
            subcall(shellcmd, flnm, fldr, flnmid)
    # 'srch' originating in 'required_by', will have a last entry called 'req'.
    if srch[-1] == "req":
        fldr = "required_files"
        # This makes it so we won't loop through the 'req' entry.
        for s in srch[:-1]:
            if s[1].startswith("python-"):
                flnm = f"{s[1]}"
            else:
                flnm = f"python-{s[0]}"
            flnmid = f"_{s[1]}"
            subcall(shellcmd, flnm, fldr, flnmid)


if __name__ == "__main__":
    yay_info()


@snoop
def pip_info(srch):
    """
    Module to extract information on
    packages from 'pip'.
    """
    shellcmd = "pip show"

    if srch[-1] == "ai":
        fldr = "data_files"
        # In this case, 'srch' will be two member tuple; the first, a
        # string with information, the second, a code to identify its
        # provenance. We only need the first.
        for i in srch[0]:
            selection = eval(i)
            flnm = f"{selection[1]}"
            flnmid = "_pip"
            subcall(shellcmd, flnm, fldr, flnmid)
    if srch[-1] == "req":
        fldr = "required_files"
        for s in srch[:-1]:
            flnm = f"{s[0]}"
            flnmid = f"_{s[1]}"
            subcall(shellcmd, flnm, fldr, flnmid)


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

    sr = fzf.prompt(allinfo)
    srch = (sr, "ai")

    pip_info(srch)
    yay_info(srch)


if __name__ == "__main__":
    srch_allinfo()


@snoop
def delete_all_files():
    """
    Deletes all files in 'data_files' and 'required_files'.
    Deletes all binary files in present directory.
    """
    for f in ["data_files", "required_files"]:
        fldr = f"{os.getcwd()}/{f}"
        fls = os.listdir(fldr)
        if fls != []:
            for i in fls:
                pth = f"{fldr}/{i}"
                os.remove(pth)

    cwd_fls = os.listdir(f"{os.getcwd()}")
    binaries = [i for i in cwd_fls if i.endswith(".bin")]
    if binaries != []:
        for b in binaries:
            os.remove(f"{os.getcwd()}/{b}")


# if __name__ == "__main__":
#     delete_all_files()


@snoop
def delete_empty_files():
    """
    Searches for entries with size 0. Deletes them.
    """
    for f in ["data_files", "required_files"]:
        fldr = f"{os.getcwd()}/{f}"
        fls = os.listdir(fldr)
        if fls != []:
            for i in fls:
                pth = f"{fldr}/{i}"
                if os.stat(pth).st_size == 0:
                    os.remove(pth)


if __name__ == "__main__":
    delete_empty_files()
