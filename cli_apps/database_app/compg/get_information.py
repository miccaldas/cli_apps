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
def run_searches(targets, interval):
    """
    User calls this function with a list of targets,
    and it will search for 10 information links per
    target.
    """
    preferential_urls = [
        "https://github.com",
        "https://linux.die.net",
        "https://pypi.org",
        "https://sourceware.org",
        "https://ftp.gnu.org",
        "https://www.commandlinux.com/man-page",
        "https://manpages.",
        "https://helpmanual.io",
        "https://man7.org/",
    ]

    avoidance_urls = [
        "netloc.endswith('.pt')",
        "https://linkedin.com",
        "https://dicion",
    ]

    userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
    app_data = []

    for name in targets:
        startpage = Startpage(name, userAgent)
        app_tuple = (name, startpage)
        app_data.append(app_tuple)
        app_data.append(interval)

        with open(f"app_data/{interval[0]}_{interval[1]}.bin", "wb") as f:
            pickle.dump(app_data, f)
        with open("tally.bin", "a") as g:
            g.write(f"{interval}\n")


@snoop
def tally(split, noman):
    """
    Where we keep count of what has already been
    analyzed and not.
    """
    noman_update = [i for i in noman if i not in split]
    with open("lists/noman.db", "wb") as f:
        pickle.dump(noman_update, f)

    length = len(noman_update)
    print(f"    There are now {length} entries to be done.")


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
    with open("lists/noman.bin", "rb") as f:
        noman = pickle.load(f)

    split = [i for i, t in enumerate(noman) if i > 50 and i <= 100]
    targets = [t for i, t in enumerate(noman) if i > 50 and i <= 100]

    run_searches(targets, [50, 100])
    tally(targets, noman)


if __name__ == "__main__":
    target_definition()
