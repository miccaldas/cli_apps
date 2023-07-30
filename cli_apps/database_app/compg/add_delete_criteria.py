"""
Module that'll facilitate adding and deleting information
from lists like preffered url's, netloc's, those to avoid
and other inofrmation of this kind.
"""
# from configs.config import Efs, tput_config
import os

# import subprocess
import pickle

import snoop
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def adc(lst, action, obj):
    """
    Given the information of what action is
    to be taken (add/delete), to what piece
    of information (string to add/delete),
    and in what list to search for it,
    ('avoid_netloc.bin', 'pref_netloc.bin'...)
    it will open the binary file, add/delete
    as the case may be, and update it.
    """
    if action == "delete":
        with open(f"lists/{lst}", "rb") as f:
            delt = pickle.load(f)
            delt.remove("obj")

    if action == "add":
        with open(f"lists/{lst}", "rb") as g:
            add = pickle.load(g)
            add.append(f"{obj}")
        os.remove(f"lists/{lst}")
        with open(f"lists/{lst}", "wb") as h:
            pickle.dump(add, h)


if __name__ == "__main__":
    adc()
