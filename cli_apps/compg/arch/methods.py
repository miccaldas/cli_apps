"""
Houses several methods to be used in building other modules.
"""
import os

# import snoop
from click import style
from rich.console import Console
from rich.padding import Padding
from snoop import pp
import pickle


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


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

    return dec


# @snoop
def print_template(text, style="bold #AAC8A7"):
    """
    Template to format string presentation.
    """
    console = Console()
    console.print(Padding(f"[{style}][+] - {text}[/]", (0, 3, 0, 10)))


# @snoop
def choice_processing(binary):
    """
    As "choice_deps" comes in as a string, that may contain one
    or more choices, and because the user can write its input
    in several ways, will try to predict some of them, and handle
    the input so to have a list of dependecies in the end.
    """

    if f"{binary}" in os.listdir(os.getcwd()):
        with open(f"{binary}", "rb") as f:
            choices = pickle.load(f)

        if " " in choices:
            choice = choices.split(" ")
        if ", " in choices:
            choice = choices.split(", ")
        if " " not in choices:
            choice = choices
        if "," in choices:
            choice = choices.split(",")

        with open("choice.bin", "wb") as g:
            pickle.dump(choice, g)
    else:
        console = Console()
        console.print(f"[bold #FFD6A5]         required_by.choice_processing():[/bold #FFD6A5] [bold #E48586]Couldn't find the {binary} file.")
        raise SystemExit
