"""
Module Docstring
"""
import os

import snoop
from snoop import pp

from location import location_main
from methods import loc_decision, pip_info, req_decision, yay_info
from required_by import choice_processing, collect_deps_info, get_lst, show


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def required_loop():
    """
    This is the structure of the loop to run
    if user only wants to see dependencies.
    """
    count = 0
    max_count = 10
    get_lst("data_files")
    while count <= max_count:
        show()
        choice_processing("choice_deps.bin")
        srch = collect_deps_info()
        yay_info(srch)
        pip_info(srch)
        gl = get_lst("required_files")
        if gl != "y":
            break

    loc = loc_decision()
    location_main()


if __name__ == "__main__":
    required_loop()
