"""
Module to deal with the leftovers of the 'analysis_app_data'
process.
"""
import os

# import subprocess
import pickle
from urllib.parse import urlparse

import snoop
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


with open("overs.bin", "rb") as g:
    overs = pickle.load(g)
lovers = list(set(overs))


@snoop
def url_searcher(url):
    """
    Function to search for links, given an url.
    """
    with open("finalized.bin", "rb") as g:
        fin = pickle.load(g)
    with open("left.bin", "rb") as f:
        left = pickle.load(f)

    final = list(set(fin))

    mansource = []
    manned_names = []
    for i in left:
        for lnk in i[1]:
            if lnk.startswith(url):
                mansource.append((i[0], lnk))
                manned_names.append(i[0])

    if url == "https://github.com":
        for g in mansource:
            if "issues" in g[1]:
                mansource.remove(g)
        for g in mansource:
            if g[0] not in g[1]:
                mansource.remove(g)

    print(mansource)
    print("\n")
    print(len(left))
    cont = input("Do you want to continue?[y/n] ")
    if cont == "n":
        raise SystemExit

    urls = []
    for i in mansource:
        up = urlparse(i[1])
        if up.path.find(i[0].capitalize()) != -1:
            urls.append((i[0], i[1]))
        if up.path.find(i[0].lower()) != -1:
            urls.append((i[0], i[1]))

    print(urls)
    cont = input("Do you want to continue?[y/n] ")
    if cont == "n":
        raise SystemExit

    final += urls
    os.remove("finalized.bin")
    with open("finalized.bin", "wb") as h:
        pickle.dump(final, h)

    os.remove("left.bin")
    nleft = [i for i in left if i[0] not in manned_names]
    with open("left.bin", "wb") as p:
        pickle.dump(nleft, p)


@snoop
def link_parse(part):
    """
    This functions accepts as input any item
    of urlparse taxonomy and will search
    for the app's name there.
    """
    with open("finalized.bin", "rb") as g:
        fin = pickle.load(g)
    with open("left.bin", "rb") as f:
        left = pickle.load(f)

    final = list(set(fin))

    site_names = []
    manned_names = []
    for f in left:
        for lnk in f[1]:
            ul = urlparse(lnk)
            if part == "path":
                if f[0] in ul.path:
                    site_names.append((f[0], lnk))
                    manned_names.append(f[0])
            if part == "netloc":
                if f[0] in ul.netloc:
                    site_names.append((f[0], lnk))
                    manned_names.append(f[0])
    final += site_names

    os.remove("finalized.bin")
    with open("finalized.bin", "wb") as h:
        pickle.dump(final, h)

    nleft = [i for i in left if i[0] not in manned_names]
    os.remove("left.bin")
    with open("left.bin", "wb") as i:
        pickle.dump(nleft, i)


@snoop
def first_link():
    """
    Given that we tok this out from a
    search engine, it would be prudent
    to heed to their knowledge and see
    what is the their first pick ofl inks.
    """
    with open("finalized.bin", "rb") as g:
        fin = pickle.load(g)
    with open("left.bin", "rb") as f:
        left = pickle.load(f)
    final = list(set(fin))

    firsts = []
    manned_names = []
    for f in left:
        for i, t in enumerate(f[1]):
            if i == 0:
                firsts.append((f[0], t))
                manned_names.append(f[0])
    final += firsts

    os.remove("finalized.bin")
    with open("finalized.bin", "wb") as h:
        pickle.dump(final, h)

    nleft = [i for i in left if i[0] not in manned_names]
    os.remove("left.bin")
    with open("left.bin", "wb") as i:
        pickle.dump(nleft, i)


if __name__ == "__main__":
    # url_searcher("https://helpmanual.io/")
    # link_parse("path")
    first_link()
