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

# import snoop
from click import style
from rich.console import Console
from rich.padding import Padding

from methods import delete_all_files, pip_info, yay_info

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def get_lst():
    """
    Iterates through the files in 'data_files'
    and looks for information on dependencies,
    if it finds that package has dependecies,
    it adds the package name and the dependecy
    name in a tuple and stores it in a list.
    """
    # All information from 'main' is stored in
    # 'data_files'. Will go there to retrieve
    # the information asked in the command line.
    reqs = f"{os.getcwd()}/data_files"
    fils = os.listdir(reqs)

    lst = []
    for file in fils:
        with open(f"{reqs}/{file}", "r") as f:
            fil = f.readlines()
            for f in fil:
                # Format found in files created by 'yay -Qi'
                if f.startswith("Required By     : "):
                    if f != f.startswith("Required By     : None\n"):
                        # The title and spaces occupy 18 px, the 20 px
                        # its that value and a small margin of confort.
                        if len(f) > 20:
                            # Deletes the title from the line. We noe have
                            # only the dependecies names.
                            deps = f[18:]
                            lst.append((file, deps))
                # Format found in files created by 'pip show'
                if f.startswith("Required-by: "):
                    if len(f) > 15:
                        deps = f[13:]
                        lst.append((file, deps))
    with open("lst.bin", "wb") as v:
        pickle.dump(lst, v)

    # The info comes with linebreaks, we strip them and eliminate
    # entries with only "None".
    cleanlst = [(a, i.strip()) for a, i in lst if i != "None\n"]
    with open("cleanlst.bin", "wb") as k:
        pickle.dump(cleanlst, k)

    # If nothing's there, it'll be mostly, for not habing found dependecies.
    # We delete the files of 'data_files' and raise systemexit().
    if cleanlst == []:
        print("The chosen packages are required by none.")
        delete_all_files()
        raise SystemExit
    # If we find dependencies, we look for empty spaces in the strings we
    # collected. If there's empty spaces it's because its a list of dependecies.
    # We split the string so as to create a list.
    else:
        spltlst = []
        for tup in cleanlst:
            if " " in tup[1]:
                if "," in tup[1]:
                    nw = (tup[0], tup[1].split(", "))
                    spltlst.append(nw)
                else:
                    nw = (tup[0], tup[1].split(" "))
                    spltlst.append(nw)
            else:
                spltlst.append(tup)

        with open("spltlst.bin", "wb") as f:
            pickle.dump(spltlst, f)


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
    with open("spltlst.bin", "rb") as t:
        deps = pickle.load(t)
    # This list will collect the id'd version of 'deps' this module will create.
    numbered_deps = []

    console = Console()
    console.print(Padding("[bold #E9FFC2]DEPENDENCIES[/]", (3, 10, 0, 10)), justify="center")
    for i in range(len(deps)):
        if deps[i][0]:
            console.print(Padding(f"[bold #AAC8A7]\n{deps[i][0][:-4]}[/]", (0, 10, 0, 10)))
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
            console.print(Padding(f"[bold #E9FFC2]\[{i}0] - {deps[i][1]}[/]", (0, 10, 0, 14)))
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

    with open("numdeps.bin", "wb") as f:
        pickle.dump(numbered_deps, f)


# @snoop
def choice_processing(binary):
    """
    As "choice_deps" comes in as a string, that may contain one
    or more choices, and because the user can write its input
    in several ways, will try to predict some of them, and handle
    the input so to have a list of dependecies in the end.
    """
    try:
        with open(f"{binary}", "rb") as f:
            choice_deps = pickle.load(f)

        if " " in choice_deps:
            choice = choice_deps.split(" ")
        if ", " in choice_deps:
            choice = choice.deps.split(", ")
        if " " not in choice_deps:
            choice = choice_deps
        else:
            if "," in choice_deps:
                choice = choice_deps.split(",")

        with open("choice.bin", "wb") as g:
            pickle.dump(choice, g)
    except Exception as e:
        print(f"An error occurred: {e}")


# @snoop
def collect_deps_info():
    """
    Collects information on the chosen dependendecies.
    """
    with open("numdeps.bin", "rb") as f:
        numdeps = pickle.load(f)

    with open("choice.bin", "rb") as g:
        choice = pickle.load(g)

    print(f"choice is {choice}")
    print(f"numdeps is {numdeps}")

    srch = [(numdeps[i][1], numdeps[i][2]) for i in range(len(numdeps)) if numdeps[i][0] in choice]
    # This will add a code to the 'srch' list that'll allow 'yay_info'
    # and 'pip_info' to know what is the internal structure of 'srch',
    # that is very different from that that is created by 'srch_allinfo'
    # when called by 'main'.
    srch.append("req")
    return srch


# @snoop
def required_main():
    """
    Calls all other functions in this module.
    """
    get_lst()
    show()
    choice_processing("choice_deps.bin")
    srch = collect_deps_info()
    yay_info(srch)
    pip_info(srch)


if __name__ == "__main__":
    required_main()
