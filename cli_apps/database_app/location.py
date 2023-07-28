"""
Module that collects package location information
and gets the user there.
"""
import os
import pickle
import subprocess
from contextlib import suppress
from time import sleep

import snoop
from rich.console import Console
from rich.padding import Padding

from methods import input_decision, print_template
from required_by import choice_processing
from show_info import show_info

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def package_location(folder):
    """
    Opens local locations of a chosen
    installed package.
    """
    console = Console()
    reqs = f"{os.getcwd()}/{folder}"
    reqfiles = os.listdir(reqs)
    locations = []

    for r in reqfiles:
        with open(f"{reqs}/{r}", "r") as f:
            content = f.readlines()
            for m in range(len(content)):
                if content[0]:
                    # First line has the package name. This gets rid of the "Name: " prefix.
                    nm = content[0][6:].strip()
                if content[m].startswith("Location:"):
                    # Same as above. Getting rid of the "Location: " prefix.
                    loc = content[m][10:].strip()
                    if loc:
                        # This eliminates the identifcation suffixes, like '_yay' in 'data_files'
                        # or the name of the package that the dependecies belong to.
                        pref = f"{r.split('_')[0]}"
                        # Creates a tuple with the package name and a full link to its location.
                        locations.append((f"{pref}", f"{loc}/{nm}"))

    # We'll need to have a nemurated version of 'locations' because, two functions ahed, there'll
    # be a need to identify location paths by their index number.
    idlocs = enumerate(locations)
    with open("idlocs.bin", "wb") as d:
        pickle.dump(idlocs, d)

    if locations != []:
        console.print(
            Padding("[bold]CHOOSE WHERE YOU WANT TO GO:[/]", (3, 10, 2, 10)),
            justify="center",
        )

        for idx, pth in enumerate(locations):
            console.print(Padding(f"\n[bold]{pth[0].upper()}[/]", (0, 10, 0, 10)))
            console.print(Padding(f"[bold]\[{idx}][/] - [bold]{pth[1]}[/]", (0, 10, 0, 10)))
        print("\n")
        visits = input_decision("Choose a number(s) to visit. Press 'Enter' to leave:")
        with open("visits.bin", "wb") as f:
            pickle.dump(visits, f)
        print("\n\n")
    else:
        print_template(f"We couldn't find any information regarding Locations for these files: {reqfiles}")
        sleep(0.3)
        with suppress(SystemError, FileNotFoundError):
            raise SystemError


# @snoop
def dislocation():
    """
    Where we open a file or, in case it's
    a folder, just see its contents.
    """

    with open("idlocs.bin", "rb") as g:
        idlocs = pickle.load(g)

    choice_processing("visits.bin")
    # 'choice.bin' is the outpu of "choice_processing"
    with open("choice.bin", "rb") as v:
        choice = pickle.load(v)

    chc = [int(i) for i in choice]

    # 't' is composed of package name and path. We only need the latter.
    pths = [t[1] for i, t in idlocs if i in chc]

    for pth in pths:
        if os.path.exists(pth):
            if os.path.isfile(pth):
                cmd = f"vim {pth}"
                subprocess.run(cmd, shell=True)
            if os.path.isdir(pth):
                # If I used the standard way of opening a with statement
                # and putting the write orders there, I couldn't put the
                # paths to the locations atop of the 'ls -l' output. It
                # turns out that, ven if you put it first, a write order
                # inside a 'with' statement, in comparison with a
                # substring command in the same place, will always run
                # after the subprocess one. I imagine that the write order
                # is only given when closing the statement. So, I had to
                # turn to this very cumbersome method of assuring that
                # things went inthe desired order.
                p = open("dirpath.txt", "a")
                p.write(f"{pth}")
                p.close()
                v = open("dirpath.txt", "a")
                v.write("\n")
                v.close()
                cmd = f"ls -l {pth} >> dirpath.txt"
                subprocess.run(cmd, shell=True)
                u = open("dirpath.txt", "a")
                u.write("\n")
                u.close()
        else:
            print_template(f"The path {pth} does not exist.")
            sleep(0.3)
            with suppress(SystemError, FileNotFoundError):
                raise SystemError


# @snoop
def open_dirs_files(result):
    """
    Asks if the user wants to open any of
    the files presented in 'dirpath.txt'.
    If yes, it opens it in a editor.
    """
    fil = input_decision("choose a file to open: ")
    fllst = []
    paths = []

    # 'fil returns a string. If it has spaces in it, it's beccause
    # it's a list.
    if " " in fil:
        # In the 'required_by' module, I created a function,
        # 'choice_processing, 'that turns strings with entries
        # separated by spaces, in lists of strings. It receives
        # a binary file and outputs another.
        with open("fil.bin", "wb") as f:
            pickle.dump(fil, f)
        choice_processing("fil.bin")
        with open("choice.bin", "rb") as g:
            fllst = pickle.load(g)
    # The id's in the presentation are structured in the following
    # way, each location path has its own enumerated is, say: 0, 1,
    # 2, for example, and the each line representing a file in said
    # location has an id that is composed of, first, the id of the
    # location, and second, its own id inside the list of files in
    # said path. Let's say we have a location that is the second one
    # in the location list. That means that its id will be '1'. Let's
    # say that a file is insode this location and it's, also, the
    # second file on its list. That'll mean that its id will '11'.One
    # for its location id, and One for its own.
    for fl in fllst:
        result_idx = int(fl[0])
        sublst_idx = int(fl[1:])
        # With these two numbers we can reconstruct the id's of the original
        # list, and access them with ease.
        # 'chc' will be a line like this:
        # "-rw-r--r-- 1 mic mic 18560 May 20 18:21 cookies.py"
        # We just want to file name, so we split the string in spaces and
        # collect the last one.
        chc = result[result_idx][sublst_idx]
        splt = chc.split(" ")
        file = splt[-1].strip()
        # To facilitate the presentation of data, the lists were not stripped
        # of linebreaks. We do that here.
        path = f"{result[result_idx][0].strip()}/{file}"
        paths.append(path)
        for p in paths:
            subprocess.run(f"vim {p}", shell=True)
    # In case of being just one choice.
    if " " not in fil:
        result_idx = int(fil[0])
        sublst_idx = int(fil[1:])
        chc = result[result_idx][sublst_idx]
        splt = chc.split(" ")
        file = splt[-1].strip()
        path = f"{result[result_idx][0].strip()}/{file}"
        subprocess.run(f"sudo vim {path}", shell=True)


# @snoop
def show_dirpath():
    """
    Prettifies the output in 'dirpath.txt'
    """
    results = []
    temp_lst = []
    console = Console()

    # When the link doesn't exist, it creates this error, that is unnecessary
    # because we know what's wrong by other means.
    with suppress(FileNotFoundError):
        with open("dirpath.txt", "r") as f:
            dirs = f.readlines()

    # To separate each directory output for presentation
    # purposes, we're going to create sublists with only
    # the content of one directory. As we know that
    # there's a blank line separating each directory,
    # we'll create a final and a temporary list. The
    # temporary one will be appending all the entries it
    # finds. If it finds a line that is only a linebreak,
    # the final list will append all content of the temporary.
    # Wich is immediately emptied of previous content, so it
    # can start the process of finding the new folder entry.
    for i in dirs:
        if i == "\n":
            temp_lst.append(i)
            results.append(temp_lst)
            temp_lst = []
        else:
            temp_lst.append(i)

    console.print(Padding("[bold]LOCATIONS[/]", (3, 10, 0, 10)), justify="center")
    for idx, r in enumerate(results):
        # 'results' is a list of lists. One for each location. That's why we
        # have this additional step.
        for i, t in enumerate(r):
            # This defines the formatting for the line that has the path.
            if t.startswith("/"):
                console.print(
                    Padding(
                        f"[bold #A0C49D][link=file://{t.strip()}]\n{t.strip()}[/link][/]",
                        (0, 10, 0, 10),
                    )
                )
            # This corresponds to the file lines.
            if t.startswith("-r"):
                console.print(Padding(f"[bold]\[{idx}{i}]   {t.strip()}[/]", (0, 10, 0, 10)))
            # And this is a 'total' line, that I don't know what it does, and tried
            # very hard to get rid of it. But it seemed to only make maatters worst.
            # So there it is.
            if t.startswith("total"):
                console.print(Padding(f"[bold]{t.strip()}[/]", (0, 10, 0, 10)))
    print("\n\n")

    open_dirs_files(results)

    os.remove("dirpath.txt")
    os.remove("idlocs.bin")
    os.remove("choice.bin")
    os.remove("visits.bin")


def location_main(folder):
    """
    Calls all other functions.
    """
    package_location(folder)
    dislocation()
    show_dirpath()


if __name__ == "__main__":
    location_main()