"""
Module Docstring
"""
import os
import pickle
import subprocess

import snoop
from pynput.keyboard import Controller, Key
from rich.console import Console
from rich.padding import Padding
from snoop import pp

from methods import input_decision
from required_by import choice_processing
from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def package_location():
    """
    Opens local locations of a chosen
    installed package.
    """
    dec = input_decision("Do you want to go to the location of a package?")
    console = Console()

    if dec == "y":
        reqs = f"{os.getcwd()}/required_files"
        reqfiles = os.listdir(reqs)
        locations = []

        for r in reqfiles:
            with open(f"required_files/{r}", "r") as f:
                content = f.readlines()
                for m in range(len(content)):
                    if content[0]:
                        nm = content[0][6:].strip()
                    if content[m].startswith("Location:"):
                        loc = content[m][10:].strip()
                        if loc:
                            pref = f"{r.split('_')[0]}"
                            locations.append((f"{pref}", f"{loc}/{nm}"))

        print(locations)
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
                console.print(
                    Padding(f"[bold]\[{idx}][/] - [bold]{pth[1]}[/]", (0, 10, 0, 10))
                )
            print("\n")
            visits = input_decision(
                "Choose a number(s) to visit. Press 'Enter' to leave:"
            )
            with open("visits.bin", "wb") as f:
                pickle.dump(visits, f)
            print("\n\n")


def choicecall():
    """
    If I called choice_processing from inside
    'dislocation', the process ended when
    'choice_processing' ended.
    To avoid this, I'm isolating the call here.
    """
    choice_processing("visits.bin")


@snoop
def dislocation():
    """
    Where we open a file or folder
    and go there.
    """
    with open("choice.bin", "rb") as f:
        choice = pickle.load(f)

    with open("idlocs.bin", "rb") as g:
        idlocs = pickle.load(g)

    print(choice)
    if len(choice) > 1:
        chc = [int(i) for i in choice]

    pths = [t[1] for i, t in idlocs if i in chc]

    keyboard = Controller()
    for pth in pths:
        if os.path.exists(pth):
            if os.path.isfile(pth):
                cmd = f"vim {pth}"
                subprocess.run(cmd, shell=True)
        if os.path.isdir(pth):
            keyboard.type(f"{pth}")
            cmd = f"ls -l {pth}"
            subprocess.run(cmd, shell=True)


if __name__ == "__main__":
    # package_location()
    # choicecall()
    dislocation()
