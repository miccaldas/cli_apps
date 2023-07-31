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
deb = os.getenv("deb")
hlp = os.getenv("HLP")
mn7 = os.getenv("MN7")


# @snoop
def localfiles():
    """
    If you came from "get_information", the
    'finalize.bin' and 'left.bin' don't exist but
    after runnig this function, they will.
    This is here so we can verify their existence.
    """
    filelst = os.listdir(comp)
    print(filelst)

    return filelst


# @snoop
def define_final(app_data=None):
    """
    Checks for existence of the 'finalized.bin'.
    If it's there it's loaded to a list, if not,
    it outputs an empty list.
    """
    filelst = localfiles()

    # Using set() makes loops much faster.
    if "finalized.bin" in set(filelst):
        with open(f"{comp}finalized.bin", "rb") as g:
            fin = pickle.load(g)
        # Turn it back to list as they're easier to deal.
        final = list(fin)
    else:
        final = []

    return final


@snoop
def define_left(app_data=None):
    """
    Checks for existence of left.bin'. If it's there
    it loaded to a list, if not, it uses the value
    given by the user in the 'app_data' argument as
    source for the list that would come from
    'left.bin'.
    """
    filelst = localfiles()

    if "left.bin" in set(filelst):
        with open(f"{comp}left.bin", "rb") as f:
            lft = pickle.load(f)
        left = list(lft)
    if app_data:
        with open(f"{appdata}{app_data}", "rb") as j:
            all_left = pickle.load(j)
            txt = "You seem to be beginning a new batch of apps. Do you want to create a new 'interval.bin'?[y/n] "
            interval_decision = input_decision(txt, color=(145, 200, 228))
            if interval_decision == "y":
                interval = all_left[-1]
                interval_str = f"{interval[0]}_{interval[1]}_results.bin"
                with open(f"{comp}interval.bin", "wb") as q:
                    pickle.dump(interval_str, q)
                left = all_left[:-1]

    return left


# @snoop
def update_finalized(nfinal):
    """
    Updates the contents of the
    'finalized.bin'.
    """
    filelst = localfiles()

    if "finalized.bin" in set(filelst):
        # "trash-put" was preffred to os.remove() as permits retrieving the erased files.
        # We're using subprocess_check_output() function, that can be used to detect error
        # messages not from Python.
        try:
            subprocess.check_output("/usr/bin/trash-put finalized.bin", cwd=comp, shell=True)
        except subprocess.CalledProcessError as e:
            print("Unable to trash file ", e.output)
            raise SystemExit
    with open(f"{comp}finalized.bin", "wb") as h:
        pickle.dump(nfinal, h)


# @snoop
def update_left(left, manned_names):
    """
    Updates the contents of left.bin'.
    """
    filelst = localfiles()

    if "left.bin" in set(filelst):
        # From the list of apps still to process, we delete those we processed now.
        nleft = [i for i in left if i[0] not in manned_names]
        # This block specifies what to do if we already processed all apps.
        if len(nleft) == 0:
            close = input_decision(
                "All apps in 'left' were treated. Do you want to close the analysis?[y/n]",
                (145, 200, 228),
            )
            if close == "y":
                with open(f"{comp}interval.bin", "rb") as w:
                    interval = pickle.load(w)
                    # We're using subprocess_check_output() function, that can be used to detect error
                    # messages not from Python.
                    try:
                        subprocess.check_output(
                            f"cp finalized.bin lists/{interval}",
                            cwd=comp,
                            shell=True,
                        )
                    except subprocess.CalledProcessError as e:
                        print("Unable to copy file ", e.output)
                        raise SystemExit
                # These deletes are just good house-keeping. No need to put them in a 'if/else'block.
                binaries = ["finalized.bin", "left.bin", "interval.bin"]
                for binary in binaries:
                    subprocess.run(f"/usr/bin/trash-put {binary}", cwd=comp, shell=True)
        # Block explaining what to do in case we still have apps to process.
        if len(nleft) != 0:
            try:
                subprocess.check_output("/usr/bin/trash-put left.bin", cwd=comp, shell=True)
            except subprocess.CalledProcessError as e:
                print("Unable to trash file ", e.output)
                raise SystemExit
            with open(f"{comp}left.bin", "wb") as p:
                pickle.dump(nleft, p)

    if "left.bin" not in filelst:
        nleft = left
        with open(f"{comp}left.bin", "wb") as p:
            pickle.dump(nleft, p)


@snoop
def url_searcher(url, app_data=None):
    """
    Function to search for links, given an url.
    """
    final = define_final(app_data)
    left = define_left(app_data)

    mansource = []
    manned_names = []
    for i in left:
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
    print("\n")
    print(len(left))
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
    with open(f"{comp}interval.bin", "rb") as k:
        interval = pickle.load(k)
    if interval != [] and len(interval) > 3:
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
        if url == "https://man7.org/":
            fldr = mn7
        with open(f"{fldr}/urls_{interval[:-12]}.bin", "wb") as f:
            pickle.dump(urls, f)

    final += urls
    # the 'final' list is, for reasons unknown, creating repeated
    # entries. Because I'm lazy, instead of understanding why, we
    # just pass it through set() to eliminate them.
    nfinal = list(set(final))

    update_finalized(nfinal)
    update_left(left, manned_names)


if __name__ == "__main__":
    url_searcher()


# @snoop
def link_parse(part, app_data=None):
    """
    This functions accepts as input any item
    of urlparse taxonomy and will search
    for the app's name there.
    """
    final = define_final(app_data)
    left = define_left(app_data)

    site_names = []
    manned_names = []
    for f in left:
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

    # We'll send it also to the 'mixed' scrapy project, that houses
    # selections not made by site.
    with open(f"scrapy/mixed/urlparse_{part}.bin", "wb") as f:
        pickle.dump(site_names, f)

    final += site_names
    # the 'final' list is, for reasons unknown, creating repeated
    # entries. Because I'm lazy, instead of understanding why, we
    # just pass it through set() to eliminate them.
    nfinal = list(set(final))

    update_finalized(nfinal)
    update_left(left, manned_names)


# if __name__ == "__main__":
#     link_parse()


# @snoop
def first_link(app_data=None):
    """
    Given that we tok this out from a
    search engine, it would be prudent
    to heed to their knowledge and see
    what is the their first pick of links.
    """
    final = define_final(app_data)
    left = define_left(app_data)

    firsts = []
    manned_names = []
    for f in left:
        for i, t in enumerate(f[1]):
            if i == 0:
                firsts.append((f[0], t))
                manned_names.append(f[0])
    final += firsts
    nfinal = final

    # We'll send it also to the 'mixed' scrapy project, that houses
    # selections not made by site.
    with open("scrapy/mixed/first_links.bin", "wb") as f:
        pickle.dump(firsts, f)

    update_finalized(nfinal)
    update_left(left, manned_names)


# if __name__ == "__main__":
#     first_link("25_35.bin")
