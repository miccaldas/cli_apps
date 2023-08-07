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
from dotenv import load_dotenv
from pyfzf.pyfzf import FzfPrompt
from rich import print
from rich.console import Console
from rich.padding import Padding
from snoop import pp

from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])
load_dotenv()


# @snoop
def input_decision(prompt, color=(160, 196, 157)):
    """
    Template for inputs, asking the user
    for a decision. 'Rich' doesn't work
    correctly with input. Has to be 'click'.
    """
    dec = input(
        style(
            f"          {prompt} ",
            # fg=color,
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


@snoop
def checkinfo():
    """
    We'll check what 'bin' files there are,
    and make a list of their names.
    """
    da = os.getenv("DA")

    filelst = os.listdir(da)
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
    da = os.getenv("DA")

    for f in fls:
        with open(f"{da}{f}", "rb") as fl:
            partial = pickle.load(fl)
            if partial != [] and partial != "":
                for i in partial:
                    # This code allows to merge to an existing list,
                    # elements of another.
                    allinf += [i]
                allinfo = [(a, b, c, d.strftime("%d/%m/%Y"), e, f, g, h, i, j) for a, b, c, d, e, f, g, h, i, j in allinf]

                with open(f"{da}allinfo.bin", "wb") as f:
                    pickle.dump(allinfo, f)

    if allinfo == []:
        print_template("aggregate_info() couldn't find content on the available files.")
        raise SystemExit


if __name__ == "__main__":
    aggregate_info()


# @snoop
def subcall(shellcmd, flnm, fldr, flnmid, stderr):
    """
    Makes 'subprocess' calls for 'yay_info'
    and 'pip_info'. To simplify the code.
    """
    da = os.getenv("DA")

    cmd = f"{shellcmd} {flnm} > {fldr}/{flnm}{flnmid} {stderr}"
    subprocess.run(cmd, cwd=da, shell=True)


# @snoop
def yay_info(srch):
    """
    Module to extract information on
    packages from 'yay'. There are
    several types of input that come
    to this function, if it comes
    from fzf, its a string that needs
    to be evaluated to a list, if it
    comes from 'required_by', it could
    a string or a list of strings.
    """
    da = os.getenv("DA")

    shellcmd = "yay -Qi"
    # This sends stderr output to a file. The initial reason for this was
    # Pip's penchant for outputing an enormous qunatity of warning messages
    # when you call 'pip show'. To hide it, the first thought was to send it
    # to /dev/null. Then I thought that, in the midst of the spurious messages,
    # could be something that's important. Besides, I don't want to loose yay's
    # output. So a text file it is.
    stderr = " 2>> error_files/yay_stderr.txt"
    # If 'srch' comes from 'srch_allinfo', will need to evaluate the
    # output, as 'fzf' presents a list as a string. To id it,
    # 'srch_allinfo' adds, at the end of 'srch', the string 'ai'.
    # This means the format of 'srch' in this case is two element tuple
    # with a list of tuples in string format as its first element, and
    # the code 'ai' as its second.
    if srch[-1] == "ai":
        fldr = "data_files"
        datapth = f"{da}{fldr}"
        flnmid = "_yay"
        # This deletes the contents of 'data_files'. This is to ensure
        # there's no contamination between requests, whilst giving time
        # enough to play with the data. Until a new request comes in.
        cmd = f"/usr/bin/trash-put {datapth}/* 2> /dev/null"
        subprocess.run(cmd, shell=True)
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
                subcall(shellcmd, flnm, fldr, flnmid, stderr)
                # Then we'll check if the file created with its name has a
                # file size of 0. This means, most probably, that it didn't
                # find the package.
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    # If it didn't find the package, we try to search for it
                    # without the "python-" prefix.
                    flnm = f"{selection[1]}[7:]"
                    subcall(shellcmd, flnm, fldr, flnmid, stderr)
            else:
                # Here, regarding filename, it's the opposite of above. We
                # start with packages that don't have a 'python-' prefix,
                # and try to add it if they fail to be found.
                flnm = f"{selection[1]}"
                subcall(shellcmd, flnm, fldr, flnmid, stderr)
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    flnm = f"python-{selection[1]}"
                    subcall(shellcmd, flnm, fldr, flnmid, stderr)

    # 'srch' originating in 'required_by', will have a last entry called 'req'.
    if srch[-1] == "req":
        fldr = "required_files"
        datapth = f"{da}{fldr}"
        # This deletes the contents of 'required_files'. This is to ensure
        # there's no contamination between requests, whilst giving time
        # enough time to play with the data. Until a new request comes in.
        cmd = f"/usr/bin/trash-put {datapth}/* 2> /dev/null"
        subprocess.run(cmd, shell=True)
        # This makes it so we won't loop through the 'req' entry.
        for s in srch[:-1]:
            # For notess on how 'flnm' is defined, see above comments
            # from lines 142 to 161.
            if s[0].startswith("python-"):
                flnm = f"{s[0]}"
                flnmid = f"_{s[1]}"
                subcall(shellcmd, flnm, fldr, flnmid, stderr)
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    flnm = f"{s[0]}[7:]"
                    subcall(shellcmd, flnm, fldr, flnmid, stderr)
            else:
                flnm = f"{s[0]}"
                flnmid = f"_{s[1]}"
                subcall(shellcmd, flnm, fldr, flnmid, stderr)
                if os.stat(f"{datapth}/{flnm}{flnmid}").st_size == 0:
                    flnm = f"python-{s[0]}"
                    subcall(shellcmd, flnm, fldr, flnmid, stderr)


if __name__ == "__main__":
    yay_info()


# @snoop
def pip_info(srch):
    """
    Module to extract information on
    packages from 'pip'.
    """
    shellcmd = "pip show"
    stderr = " 2>> error_files/pip_stderr.txt"
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
            subcall(shellcmd, flnm, fldr, flnmid, stderr)
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
            subcall(shellcmd, flnm, fldr, flnmid, stderr)


if __name__ == "__main__":
    pip_info()


@snoop
def srch_allinfo():
    """
    Searches 'allinfo' with fzf and, if needed,
    collects user selections.
    """
    da = os.getenv("DA")
    fzf = FzfPrompt()

    with open(f"{da}allinfo.bin", "rb") as f:
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
    da = os.getenv("DA")
    mn = os.getenv("MN")

    cwd_fls = os.listdir(da)
    mngmnt_fls = os.listdir(mn)
    cwd_bins = [i for i in cwd_fls if i.endswith(".bin")]
    mngmnt_bins = [i for i in mngmnt_fls if i.endswith(".bin")]
    if cwd_bins != []:
        for b in cwd_bins:
            os.remove(f"{da}{b}")
    if mngmnt_bins != []:
        for b in mngmnt_bins:
            os.remove(f"{mn}{b}")


if __name__ == "__main__":
    delete_all_files()


# @snoop
def req_decision():
    """
    Asks the user if he wants to see the
    dependecies of any package.
    """
    console = Console()
    required = input_decision("Do you want to explore one of these package dependecies?[y/n] ")

    if required == "y":
        return "y"


if __name__ == "__main__":
    req_decision()


# @snoop
def loc_decision():
    """
    Asks the user if he wants to see the
    folder contents of a package.
    """
    console = Console()
    ailocation = input_decision("Do you want to see more on the location of these files?[y/n] ")
    if ailocation == "y":
        return "y"


if __name__ == "__main__":
    loc_decision()
