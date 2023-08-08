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


@snoop
def srch_allinfo():
    """
    Searches 'allinfo' with fzf and, if needed,
    collects user selections.
    """
    da = os.getenv("DA")
    fzf = FzfPrompt()

    allinfo = ["dog", "cat", "bird"]

    sr = fzf.prompt(allinfo)
    print(sr)
    print(type(sr))


if __name__ == "__main__":
    srch_allinfo()
