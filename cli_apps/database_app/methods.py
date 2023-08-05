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
from rich.padding import Padding
from snoop import pp

from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def input_decision(prompt, color=(160, 196, 157)):
    """
    Template for inputs, asking the user
    for a decision.
    """
    dec = input(
        style(
            f"          {prompt} ",
            fg=color,
            bold=True,
        )
    )
    print("\n")

    return dec


# @snoop
def print_template(text, style="bold #AAC8A7"):
    """
    Template to format string presentation.
    """
    console = Console()
    console.print(Padding(f"[{style}][+] - {text}[/]", (0, 3, 0, 10)))


# @snoop
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


# @snoop
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
    for t in allinf:
        print(t)
    allinfo = [(a, b, c, d.strftime("%d/%m/%Y"), e, f, g, h, i, j) for a, b, c, d, e, f, g, h, i, j in allinf]

    with open("allinfo.bin", "wb") as f:
        pickle.dump(allinfo, f)


if __name__ == "__main__":
    aggregate_info()


# @snoop
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
    # This means the format of 'srch' in this case is two element tuple
    # with a list of tuples in string format as its first element, and
    # the code 'ai' as its second.
    if srch[-1] == "ai":
        fldr = "data_files/"
        datapth = f"{os.getcwd()}/{fldr}"
        flnmid = "_yay"

        # This deletes the contents of 'data_files'. This is to ensure
        # there's no contamination between requests, whilst giving time
        # enough to play with the data. Until a new request comes in.
        cmd = f"/usr/bin/trash-put {datapth}*"
        subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)

        # In this case, 'srch' will be two member tuple; the first, a
        # string with information, the second, a code to identify its
        # provenance. We only need the first.
        for i in srch[0]:
            selection = eval(i)
            # To ensure we looked thouroughly through 'Paacman's database,
            # we'll try to look for packages in two of the ways they're
            # usually written. In this case, if the 'srch' request has a
            # package that start's with 'python-':
            if selection[1].startswith("python-"):
                # We try with this name first.
                flnm = f"{selection[1]}"
                subcall(shellcmd, flnm, fldr, flnmid)
                # Then we'll check if the file created with its name has a
                # file size of 0. This means, most probably, that it didn't
                # find the package.
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    # If it didn't find the package, we try to search for it
                    # without the "python-" prefix.
                    flnm = f"{selection[1]}[7:]"
                    subcall(shellcmd, flnm, fldr, flnmid)
            else:
                # Here, regarding filename, it's the opposite of above. We
                # start with packages that don't have a 'python-' prefix,
                # and try to add it if they fail to be found.
                flnm = f"{selection[1]}"
                subcall(shellcmd, flnm, fldr, flnmid)
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    flnm = f"python-{selection[1]}"
                    subcall(shellcmd, flnm, fldr, flnmid)
                flnm = f"python-{selection[1]}"
    # 'srch' originating in 'required_by', will have a last entry called 'req'.
    if srch[-1] == "req":
        fldr = "required_files/"
        datapth = f"{os.getcwd()}/{fldr}"

        # This deletes the contents of 'data_files'. This is to ensure
        # there's no contamination between requests, whilst giving time
        # enough to play with the data. Until a new request comes in.
        cmd = f"/usr/bin/trash-put {datapth}*"
        subprocess.run(cmd, cwd=f"{os.getcwd()}", shell=True)

        # This makes it so we won't loop through the 'req' entry.
        for s in srch[:-1]:
            # For notess on how 'flnm' is defined, see above comments
            # from lines 142 to 161.
            if s[0].startswith("python-"):
                flnm = f"{s[0]}"
                flnmid = f"_{s[1]}"
                subcall(shellcmd, flnm, fldr, flnmid)
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    flnm = f"{s[0]}[7:]"
                    subcall(shellcmd, flnm, fldr, flnmid)
            else:
                flnm = f"{s[0]}"
                flnmid = f"_{s[1]}"
                subcall(shellcmd, flnm, fldr, flnmid)
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    flnm = f"python-{s[0]}"
                    subcall(shellcmd, flnm, fldr, flnmid)


if __name__ == "__main__":
    yay_info()


@snoop
def pip_info(srch):
    """
    Module to extract information on
    packages from 'pip'.
    """
    shellcmd = "pip -qq show"
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
            flnm = f"{selection[1]}"
            flnmid = "_pip"
            subcall(shellcmd, flnm, fldr, flnmid)
    # The 'req' code tell 's us that it's a request from 'required_by'.
    # This means that is a list of tuples with a chosen package as
    # second member, and one of its dependencies as the first.
    if srch[-1] == "req":
        fldr = "required_files"
        # The last element of 'srch' is the provenance code 'req'.
        # We don't need it for this.
        for s in srch[:-1]:
            flnm = f"{s[0]}"
            flnmid = f"_{s[1]}"
            subcall(shellcmd, flnm, fldr, flnmid)


if __name__ == "__main__":
    pip_info()


# @snoop
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

    yay_info(srch)
    pip_info(srch)


if __name__ == "__main__":
    srch_allinfo()


# @snoop
def delete_all_files():
    """
    Deletes all binary files in present directory and 'mngmnt'.
    """

    cwd_fls = os.listdir(f"{os.getcwd()}")
    mngmnt_fls = os.listdir(f"{os.getcwd()}/mngmnt")
    cwd_bins = [i for i in cwd_fls if i.endswith(".bin")]
    mngmnt_bins = [i for i in mngmnt_fls if i.endswith(".bin")]
    if cwd_bins != []:
        for b in cwd_bins:
            os.remove(f"{os.getcwd()}/{b}")
    if mngmnt_bins != []:
        for b in mngmnt_bins:
            os.remove(f"{os.getcwd()}/mngmnt/{b}")


if __name__ == "__main__":
    delete_all_files()


# @snoop
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
                # 'os.stat(pth)' corresponds to all metadata.
                # 'sr_size' is file size.
                if os.stat(pth).st_size == 0:
                    os.remove(pth)


if __name__ == "__main__":
    delete_empty_files()


# @snoop
def alternative_presentations(tag="ai"):
    """
    Presents, at screens showing info
    from 'data_files' or 'required_files',
    other options of search. At this time
    they are: location and dependecies.
    """

    if tag == "ai":
        required = input_decision("Do you want to explore one of these package dependecies?[y/n] ")
        if required == "y":
            alternative = "required_by"
        ailocation = input_decision("Do you want to see more on the location of these files?[y/n] ")
        if ailocation == "y":
            alternative = "location_main"
        if required == "y" and ailocation == "y":
            alternative = ("required_by", "location_main")
        ext = input_decision("Do you want to exit the session?[y/n] ")
        if ext == "y":
            alternative = "exit"

    if tag == "req":
        location = input_decision("Do you want to see more on the location of these files?[y/n] ")
        if location == "y":
            alternative == "location"

    return alternative


if __name__ == "__main__":
    alternative_presentations()
