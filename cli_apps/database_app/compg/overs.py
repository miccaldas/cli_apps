"""
Module to deal with the leftovers of the 'analysis_app_data'
process.
"""
# import os
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


with open("app_data/0_50.bin", "rb") as f:
    ur = pickle.load(f)
overdata = []
for i in ur:
    if i[0] in lovers:
        overdata.append(i)


with open("finalists.bin", "rb") as h:
    final = pickle.load(h)


@snoop
def linux_die():
    """
    We look for links from 'linux.die.net'.
    If we find it, we take them out of the
    list and consider this app as ready to
    spider.
    """
    mansource = []
    manned_names = []
    for i in overdata:
        for lnk in i[1]:
            if lnk.startswith("https://linux.die.net"):
                mansource.append((i[0], lnk))
                manned_names.append(i[0])

    mansource += final
    with open("finalized.bin", "wb") as s:
        pickle.dump(mansource, s)

    left = [i for i in overdata if i[0] not in manned_names]
    with open("left.bin", "wb") as p:
        pickle.dump(left, p)


if __name__ == "__main__":
    linux_die()
