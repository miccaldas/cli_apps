"""
Module to select the best sources of knowledge
for the scrapy spiders.
"""
import os
import pickle
import subprocess
from urllib.parse import urlparse

import snoop
from cli_apps.database_app.methods import input_decision
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])
load_dotenv()

# Envs
appdata = os.getenv("APPDATA")
comp = os.getenv("COMP")
git = os.getenv("GIT")
pip = os.getenv("PIP")
src = os.getenv("SRC")
die = os.getenv("DIE")
gnu = os.getenv("GNU")
cmd = os.getenv("CMD")
deb = os.getenv("DEB")
hlp = os.getenv("HLP")
mn7 = os.getenv("MN7")


@snoop
def url_searcher(url, app_data):
    """
    Function to search for links, given an url.
    """
    with open(f"{comp}epoch.bin", "rb") as d:
        ep = pickle.load(d)
    low = ep[0]
    upp = ep[1]

    with open(f"{app_data}", "rb") as u:
        appdata = pickle.load(u)
        app_data = appdata[:-1]

    mansource = []
    manned_names = []
    for i in app_data:
        for lnk in i[1]:
            if lnk.startswith(url):
                mansource.append((i[0], lnk))
                manned_names.append(i[0])

    if url == "https://github.com":
        for g in set(mansource):
            if "issues" in g[1]:
                mansource.remove(g)
        for g in set(mansource):
            if g[0] not in g[1]:
                mansource.remove(g)

    print(mansource)
    cont = input_decision("Do you want to continue?[y/n] ", (145, 200, 228))
    if cont == "n":
        raise SystemExit

    urls = []
    for i in set(mansource):
        up = urlparse(i[1])
        # The next code bolck is here to search for the
        # app's name in the url's path capitalized or
        # in lower letters. We're using find() instead
        # of just the in() clause, because when we did
        # use it, it gave false positives. find() has
        # correct all the time. The result must be
        # different than '-1' because that's what find()
        # outputs when it has a negative result.
        if up.path.find(i[0].capitalize()) != -1:
            urls.append((i[0], i[1]))
        if up.path.find(i[0].lower()) != -1:
            urls.append((i[0], i[1]))

    print(urls)
    cont = input_decision("Do you want to continue?[y/n] ", (145, 200, 228))
    if cont == "n":
        raise SystemExit

    # As we're going to create different projects for different sites, we'll
    # send the url's pertaining to a site, to their folder.
    with open(f"{comp}epoch.bin", "rb") as k:
        interval = pickle.load(k)
    if interval != [] and len(interval) == 2:
        if url == "https://github.com":
            fldr = git
        if url == "https://linux.die.net":
            fldr = die
        if url == "https://pypi.org":
            fldr = pip
        if url == "https://sourceware.org":
            fldr = src
        if url == "https://ftp.gnu.org":
            fldr = gnu
        if url == "https://www.commandlinux.com":
            fldr = cmd
        if url == "https://manpages.debian":
            fldr = deb
        if url == "https://helpmanual.io":
            fldr = hlp
        if url == "https://man7.org":
            fldr = mn7
        with open(f"{fldr}/urls_{low}_{upp}.bin", "wb") as f:
            pickle.dump(urls, f)


if __name__ == "__main__":
    url_searcher()


# @snoop
def link_parse(part, app_data, destination):
    """
    This functions accepts as input any item
    of urlparse taxonomy and will search
    for the app's name there.
    """

    site_names = []
    manned_names = []
    for f in app_data:
        # The reason we're using set() to speed the loop in 'f[1]'
        # but not in 'left', it's because 'left' has lists inside
        # its tuples. Although set() accepts tuples, it doesn't
        # accept lists.
        for lnk in set(f[1]):
            ul = urlparse(lnk)
            if part == "path":
                if f[0] in ul.path:
                    site_names.append((f[0], lnk))
                    manned_names.append(f[0])
            if part == "netloc":
                if f[0] in ul.netloc:
                    site_names.append((f[0], lnk))
                    manned_names.append(f[0])

    with open(f"{destination}/link_parse.bin", "wb") as f:
        pickle.dump(site_names, f)


if __name__ == "__main__":
    link_parse()


# @snoop
def first_link(app_data, destination):
    """
    Given that we tok this out from a
    search engine, it would be prudent
    to heed to their knowledge and see
    what is the their first pick of links.
    """

    firsts = []
    manned_names = []
    for f in app_data:
        for i, t in enumerate(f[1]):
            if i == 0:
                firsts.append((f[0], t))
                manned_names.append(f[0])

    with open(f"{destination}/first_links.bin", "wb") as f:
        pickle.dump(firsts, f)


if __name__ == "__main__":
    first_link("25_35.bin")
