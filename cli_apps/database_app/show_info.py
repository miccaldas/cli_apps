"""
A ready made structure, to be used to view the collected data
in the cli.
"""
import os
import pickle
import subprocess

from dotenv import load_dotenv

# import snoop
from rich import print
from rich.console import Console
from rich.padding import Padding

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
load_dotenv()


# @snoop
def show_info(folder, title):
    """
    We look in the data_file, to see what packages have
    information available on them, we create links of
    their location, so we can show their content. We use
    Rich to get a better look.
    """
    da = os.getenv("DA")
    console = Console()

    cwd = os.getenv("DA")
    data = folder
    file_names = os.listdir(data)

    # List to house the links that'll create based on 'file_names'.
    lnks = []
    for name in file_names:
        lnk = f"{data}/{name}"
        lnks.append(lnk)

    for lnk in lnks:
        # Checking for file size, if it's zero, we pop it
        # out of the list.:
        stt = os.stat(lnk)
        if stt.st_size == 0:
            console.print(Padding(f"[bold #E48586]The file {lnk} as 0 size. Deleted.", (3, 10, 0, 10)))
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
