"""
Module to detect and replace url's known
to be dead or not have good information,
and detect and replace missing entries.
"""
import os
import pickle

import snoop
from ScrapeSearchEngine.ScrapeSearchEngine import Startpage
from snoop import pp

from methods import print_error
from websrch import websrch

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


@snoop
def alternative_urls() -> None:
    """
    There are some url's that don't produce scraping results,
    we look for them in *nospaces.bin* and search the web for
    alternatives that we know will yield results. If we find
    them, we alter the url value.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data/"
    with open(f"{pip}nospaces.bin", "rb") as f:
        newurls: list[list[str]] = pickle.load(f)

    changers: list[list[str]] = [
        u
        for u in newurls
        if u[2].startswith("https://pagure.io")
        or u[2].startswith("http://www.voidspace.org.uk")
        or u[2].startswith("https://ieee1394.wiki.kernel.org")
        or u[2].startswith("https://sf.net")
        or u[2].startswith("/")
        or "sourceforge" in u[2]
        or "canonware" in u[2]
    ]

    userAgent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"

    if changers != []:
        for u in changers:
            name = u[0]
            # There's a 'Scrape Search Engine' package, that does web searches in chosen searchengines
            # programatically. I added 'Startpage' to its list of engines, and that's what we're using.
            # It requires a userAgent value, so as not to be shunned by the engines. I put my own.
            # The function that does the work is 'websrch', in the 'b_upld' module.
            res: list[str] = websrch(name)
            if res != []:
                # We'll delete the entries with the old url and replace them with the new one.
                for n, c in enumerate(newurls):
                    if newurls[n][0] == name:
                        newurls[n].pop(2)
                        newurls[n].append(res[0])

    with open(f"{pip}alturls.bin", "wb") as f:
        pickle.dump(newurls, f)


if __name__ == "__main__":
    alternative_urls()


# @snoop
def xorg_urls() -> None:
    """
    Xorg_urls for Yay packages.
    All Xorg packages have as URL, a generic *Freedesktop* site
    url, which won't bring much information. We replace them
    with url's to their *Github* pages.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data/"
    namesfile: str = f"{pip}alturls.bin"

    with open(namesfile, "rb") as f:
        newnames: list[list[str]] = pickle.load(f)

    newurls: list[list[str]] = []
    for entry in newnames:
        if entry[2].startswith("https://github.com/freedesktop"):
            if entry[0].startswith("xorg-"):
                ent = entry[0][5:]
            if entry[0].startswith("xorg") and "-" not in entry[0]:
                ent = entry[0][4:]
            else:
                ent = entry[0]
            if "driver" in entry[1]:
                newurl = f"https://gitlab.freedesktop.org/xorg/driver/{ent}"
            if "documentation" in entry[1]:
                newurl = f"https://gitlab.freedesktop.org/xorg/doc/{ent}"
            if "proto" in ent:
                newurl = f"https://gitlab.freedesktop.org/xorg/proto/{entry[0]}"
            if "lib" in ent:
                newurl = f"https://gitlab.freedesktop.org/xorg/lib/{ent}"
            if "driver" not in entry[1] and "documentation" not in entry[1] and "lib" not in ent and "proto" not in ent:
                newurl = f"https://gitlab.freedesktop.org/xorg/util/{ent}"
            newurls.append([entry[0], entry[1], newurl])
        else:
            newurls.append(entry)

    with open(f"{pip}newurls.bin", "wb") as v:
        pickle.dump(newurls, v)


if __name__ == "__main__":
    xorg_urls()


# @snoop
def len_check() -> None:
    """
    We'll check the length of the entries in 'newurls.bin'
    to see if every field is filled. If not:
    We'll try to find a new link for the 'url' field, if not
    successful, we'll fill it with dummy text, and send an
    alert about the situation.
    If it's the 'presentation' field, we'll use dummy text,
    and alert the user we're using dummy text for that entry.
    If the field is 'name', we'll send an alert and raise
    'SystemExit'.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data/"
    with open(f"{pip}newurls.bin", "rb") as f:
        ns: list[list[str]] = pickle.load(f)

    # List that gathers all entries with missing field values. If a field
    # is missing, python puts a '' sign on where it should've been.
    sht: list[list[str]] = [i for i in ns if any(i[idx] == "" for idx, t in enumerate(i))]

    # If there's entries on the missing fields list:
    if sht != []:
        for i, t in enumerate(sht):
            # If it's the 'url' field at index '2':
            if sht[i][2] == "":
                # call the 'websrch' function, to look for links with the package's name. Index '0'.
                res: list[str] = websrch(sht[i][0])
                # If it's successfull, delete the the former entry and replace it by the found link.
                if res != []:
                    sht[i].pop(2)
                    sht[i].append(res[0])
                # If 'websrch' was not successful at finding a link, write some boilerplate string on
                # the field and alert the user.
                else:
                    sht[i].pop(2)
                    sht[i].append("Provisional Text.")
                    print_error(
                        f"The 'url' field in [bold #C4C1A4]{sht[i][0]}[/bold #C4C1A4] is empty. We tried replacing it but found nothing. We''l use provisional text until it's resolved."
                    )
            # For the 'presentation' field.
            if sht[i][1] == "":
                sht[i].pop(1)
                sht[i].insert(1, "Provisional Text.")
                print_error(f"The 'Presentation' field in [bold #C4C1A4]{sht[i][0]}[/bold #C4C1A4] has no value. We'll use provisional text until it's resolved.")
            # For the name field. This assumes a situation with more gravity. We don't try to solve it, just stop execution
            # for the user to do a manual intervention.
            if sht[i][0] == "":
                print_error(f"There's no 'Name' value at index [bold #C4C1A4]{i}[/bold #C4C1A4].  We'll stop execution until it's resolved.")
                raise SystemExit

        with open("sht.bin", "wb") as g:
            pickle.dump(sht, g)


if __name__ == "__main__":
    len_check()


# @snoop
def list_conciliation() -> None:
    """
    Updates the content of 'newurls.bin'
    with the results of 'sht.bin'
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data/"
    piplst = os.listdir(pip)
    with open(f"{pip}newurls.bin", "rb") as f:
        nn = pickle.load(f)

    if "sht.bin" in piplst:
        with open(f"{pip}/sht.bin", "rb") as j:
            st = pickle.load(j)
        for i, t in enumerate(nn):
            for id, ls in enumerate(st):
                if nn[i][0] == st[id][0]:
                    nn.pop(i)
                    nn.append(st[id])

        os.remove(f"{pip}newurls.bin")
        with open("newurls.bin", "wb") as h:
            pickle.dump(nn, h)


if __name__ == "__main__":
    list_conciliation()
