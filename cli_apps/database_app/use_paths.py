"""
Module that define the functions that'll be served
depending on user's choices. If the user chooses
'locations' or 'dependencies', it'll have different
information presented to him. We define what
information it is and in what way is shown.
At the moment I put a limit of 10 in the capacity to
ask again the same type of question. But when I feel
more sure about the workings of this solution I would
like it to be limitless.
"""
import os

import snoop
from dotenv import load_dotenv
from snoop import pp

from location import dislocation, package_location, show_dirpath
from methods import loc_decision, pip_info, req_decision, yay_info
from required_by import choice_processing, collect_deps_info, get_lst, show


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])
load_dotenv()


# @snoop
def required_loop():
    """
    This is the structure of the loop to run
    if user only wants to see dependencies.
    The basice concept is for the user to be
    able to repeat its dependencies searches
    as much as he wants, going as deep as he
    likes. You cai leave the loop if you don't
    answer the questions or, by the program's
    will, if there's a problem with the code.
    """
    da = os.getenv("DA")

    # The first call to dependencies is done when
    # there's only package files in 'data_files'.
    # After that is always in 'required_files'. We
    # needed to have a first look at the files still
    # in 'data_files'. Thatt's the reason why there's
    # a get_lst() call before the loop.
    out = get_lst(f"{da}data_files")
    if out == "y":
        for i in range(10):
            show()
            choice_processing(f"{da}choice_deps.bin")
            srch = collect_deps_info()
            yay_info(srch)
            pip_info(srch)
            # So as not to break the loop, we took out the SystemExit
            # we had for when there was an error, and replaced it with
            # 'return' statements. If there's an error get_lst()
            # returns 'n', if everything went correctly, it outputs 'y'.
            # This way the flow is controled when designing the loop,
            # making it easier to change when needed.
            gl = get_lst(f"{da}required_files")
            if gl != "y":
                break

    # After the loop has ran, we ask the user if he wants to see
    # the packages locations. In the 'location' loop it's the
    # other way around.
    loc = loc_decision()
    # If it starts after the 'required_loop' having ran, we know that
    # the last information is in 'required_files'. So we set the
    # 'location_loop' location to it.
    if loc == "y":
        location_loop(f"{da}required_files")


if __name__ == "__main__":
    required_loop()


@snoop
def location_loop(folder):
    """
    Loop for the 'location' module. Here,
    because we don't have to create data
    from one location to another, we can
    leave it for the callers of the loop
    the decision on what folder to use.
    """
    for i in range(10):
        inner = package_location(folder)
        if inner != "y":
            break
        dislocation()
        show_dirpath()

    req = req_decision()
    if req == "y":
        required_loop()


if __name__ == "__main__":
    location_loop()
