"""
Module that'll information from the web, to put in
the 'cli_apps' entries.
"""
# import os
# import subprocess
import pickle
from urllib.parse import urlparse

import snoop
from ScrapeSearchEngine.ScrapeSearchEngine import Startpage

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def run_searches(targets, epoch):
    """
    User calls this function with a list of targets,
    and it will search for 10 information links per
    target.
    """

    userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    app_data = []

    for name in targets:
        startpage = Startpage(name, userAgent)
        app_tuple = (name, startpage)
        app_data.append(app_tuple)

    app_data.append(epoch)

    with open(f"app_data/{epoch[0]}_{epoch[1]}.bin", "wb") as f:
        pickle.dump(app_data, f)


@snoop
def target_definition():
    """
    It probably won't be productive to try
    to get all seven thoused plus excutables
    in '/usr/bin' in one go. We'll split it
    in manageable quantites, and keep a
    tally of what's been done.i To do this,
    supply as information, the list of apps
    to be explored, as well as the id
    interval that we used.
    """
    with open("epoch.bin", "rb") as g:
        epoch = pickle.load(g)
    with open("lists/noman.bin", "rb") as f:
        noman = pickle.load(f)

    min = epoch[0]
    max = epoch[1]
    targets = [t for i, t in enumerate(noman) if i > f"{min}" and i <= f"{max}"]

    run_searches(targets, [f"{min}", f"{max}"])


if __name__ == "__main__":
    target_definition()
