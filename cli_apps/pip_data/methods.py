"""
Houses several methods to be used in building other modules.
"""
import os
import pickle

# import snoop
from click import style
from rich.console import Console
from rich.padding import Padding

# from snoop import pp

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def input_decision(prompt: str, color: tuple[int, int, int] = (160, 196, 157)) -> str:
    """
    Template for inputs, asking the user
    for a decision. 'Rich' doesn't work
    correctly with input. Has to be 'click'.
    """
    dec: str = input(
        style(
            f"          {prompt} ",
            # fg=color,
            bold=True,
        )
    )

    return dec


# @snoop
def print_info(text: str, style: str = "bold #176B87") -> None:
    """
    Template to format string presentation.
    """
    console = Console()
    console.print(Padding(f"[{style}]\[INFORMATION] - {text}[/]", (0, 3, 0, 10)))


# @snoop
def print_error(text: str, style: str = "bold #FF6666") -> None:
    """
    Template to format string presentation.
    """
    console = Console()
    console.print(Padding(f"[{style}]\[ERROR] - {text}[/]", (0, 3, 0, 10)))


# @snoop
def choice_processing(binary: str) -> None:
    """
    As "choice_deps" comes in as a string, that may contain one
    or more choices, and because the user can write its input
    in several ways, will try to predict some of them, and handle
    the input so to have a list of dependecies in the end.
    """
    da = "/home/mic/python/cli_apps/cli_apps/pip_data/"

    if f"{binary}" in os.listdir(da):
        with open(f"{da}{binary}", "rb") as f:
            choices: str = pickle.load(f)

        if " " in choices:
            choice = choices.split(" ")
        if ", " in choices:
            choice = choices.split(", ")
        if " " not in choices:
            # The variable, in this case changes to a string.
            # 'Mypy' doesn't accept variable reassignments, and 'choice was, before, a list.'
            choice = choice  # ignore[assignment]
            choice = choices.split(",")

        with open(f"{da}choice.bin", "wb") as g:
            pickle.dump(choice, g)
    else:
        console = Console()
        console.print(f"[bold #FFD6A5]   required_by.choice_processing():[/bold #FFD6A5] [bold #E48586]Couldn't find the {binary} file.")
        raise SystemExit
