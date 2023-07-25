"""
A ready made structure, to be used to view the collected data
in the cli.
"""
import os
import pickle
import subprocess

# import snoop
from rich import print
from rich.console import Console
from rich.padding import Padding
from rich.panel import Panel

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def show_info(folder, title):
    """
    We look in the data_file, to see what packages have
    information available on them, we create links of
    their location, so we can show their content. We use
    Rich to get a better look.
    """
    cwd = os.getcwd()
    data = f"{cwd}/{folder}"
    file_names = os.listdir(data)

    # List to house the links that'll create based on 'file_names'. We're
    # going to trust that the user knows that the files are are there and
    # make only a test, further on, to ascertain that the file is there or
    # not.
    lnks = []
    for name in file_names:
        lnk = f"{data}/{name}"
        lnks.append(lnk)

    for lnk in lnks:
        # This is the test. We check for file size, if it's zero, we pop it
        # out of the list.:
        stt = os.stat(lnk)
        if stt.st_size == 0:
            idx = lnks.index(lnk)
            lnks.pop(idx)

    # List to house the output of all the chosen files.
    fullcont = []
    for t in lnks:
        with open(t, "r") as f:
            cont = f.readlines()
            content = [i.strip() for i in cont]
            # The info of one package appeared immediately after the other.
            # List's 'insert', adds a entry at a given position, without
            # replacing nothing.
            content.insert(0, "\n")
            # The '+=' formulation, between lists, makes it so the first
            # absorbs the elements of the second one.
            fullcont += content

    console = Console()
    console.print(
        Padding(f"[bold]{title}[/]", (3, 10, 0, 10)),
        justify="center",
    )
    for line in fullcont:
        if line.startswith("Location: "):
            console.print(Padding(f"[red]{line}[/]", (0, 10, 0, 10)))
        else:
            console.print(Padding(f"{line}", (0, 10, 0, 10)))

    console.print("\n\n")


if __name__ == "__main__":
    show_info()
