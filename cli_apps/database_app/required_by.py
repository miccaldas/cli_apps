"""
This modules probes the packages that depend on given package.
A lot of times I don't don't know if a dependecy is a live
event or a fossil of a bygone era. This will help bring clarity
to these questions. This won't be so directed to immediate
consumption, we created a directory to house the data, that the
user can check any time. It'll be a more mediated experience.
"""
import os
import pickle

import snoop
from click import style
from rich.console import Console
from rich.padding import Padding
from snoop import pp

from methods import pip_info, srch_allinfo, yay_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def get_lst():
    """"""
    reqs = f"{os.getcwd()}/required_files"
    fils = os.listdir(reqs)

    lst = []
    for file in fils:
        with open(f"{reqs}/{file}", "r") as f:
            fil = f.readlines()
            for f in fil:
                if f.startswith("Required By     : "):
                    if f != f.startswith("Required By     : None"):
                        if len(f) > 20:
                            deps = f[18:]
                            lst.append((file, deps))
    cleanlst = [(a, i.strip()) for a, i in lst if i != "None\n"]

    spltlst = []
    for tup in cleanlst:
        if " " in tup[1]:
            nw = (tup[0], tup[1].split())
            spltlst.append(nw)
        else:
            spltlst.append(tup)

    return spltlst


if __name__ == "__main__":
    get_lst()


# @snoop
def show():
    """
    Visualizes the results.
    We use used mostly *Rich* to views results,
    except in the *input* method. Although 'rich'
    has their own implementation of 'input', it
    shows the prompt one line below the text and
    pressed to the border of the screen.
    """
    deps = get_lst()
    # This list will collect the id'd version of 'deps' this module will create.
    numbered_deps = []

    console = Console()
    console.print(
        Padding("[bold #E9FFC2]DEPENDENCIES[/]", (3, 10, 0, 10)), justify="center"
    )
    for i in range(len(deps)):
        if deps[i][0]:
            console.print(
                Padding(f"[bold #AAC8A7]\n{deps[i][0][:-4]}[/]", (0, 10, 0, 10))
            )
        if type(deps[i][1]) == list:
            for idx, t in enumerate(deps[i][1]):
                # collects a dependency id made of the index of the chosen package,
                # plus the index of the dependecy. This permits us to know what is
                # the package and dependecy name.
                numdp = [f"{i}{idx}", f"{t}", f"{deps[i][0][:-4]}"]
                numbered_deps.append(numdp)
                console.print(
                    Padding(
                        f"[bold #FFD6A5]\[{i}{idx}] - [/][bold #E9FFC2]{t}[/]",
                        (0, 10, 0, 14),
                    )
                )
        else:
            console.print(
                Padding(f"[bold #E9FFC2]\[{i}0] - {deps[i][1]}[/]", (0, 10, 0, 14))
            )
            numdp = [f"{i}0", f"{deps[i][1]}", f"{deps[i][0][:-4]}"]
            numbered_deps.append(numdp)

    print("\n")
    choice_deps = input(
        style(
            "          Choose the dependecies you want to see. Press Enter to quit. ",
            bold=True,
            fg=(160, 196, 157),
        )
    )
    console.print("\n\n")

    with open("choice_deps.bin", "wb") as g:
        pickle.dump(choice_deps, g)

    return numbered_deps


@snoop
def choice_processing():
    """
    As "choice_deps" comes in as a string, that may contain one
    or more choices, and because the user can write its input
    in several ways, will try to predict some of them, and handle
    the input so to have a list of dependecies in the end.
    """
    with open("choice_deps.bin", "rb") as f:
        choice_deps = pickle.load(f)

    if " " in choice_deps:
        choice = choice_deps.split(" ")
    if ", " in choice_deps:
        choice = choice.deps.split(", ")
    if " " not in choice_deps:
        if len(choice_deps) == 2:
            choice = choice_deps
        else:
            if "," in choice_deps:
                choice = choice_deps.split(",")

    # choice = [int(i) for i in chc]

    return choice


@snoop
def collect_deps_info():
    """
    Collects information on the chosen dependendecies.
    """
    numdeps = show()
    choice = choice_processing()

    print(f"choice is {choice}")
    print(f"numdeps is {numdeps}")

    lst = [
        (numdeps[i][2], numdeps[i][1])
        for i in range(len(numdeps))
        if numdeps[i][0] in choice
    ]

    # yay_info(lst)
    pip_info(lst)


if __name__ == "__main__":
    collect_deps_info()

# srch_allinfo()
# get_lst()
