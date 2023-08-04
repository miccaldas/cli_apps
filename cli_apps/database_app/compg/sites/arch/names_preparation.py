"""
Module to prepare the file that'll house
all information entries to use on the
Scrapy project.
"""
import os
import pickle
import shutil

import snoop
from cli_apps.database_app.compg.link_analysis import first_link
from dotenv import load_dotenv
from snoop import pp

from epilogue import copy_files, delete_files, epoch_counting_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])
load_dotenv()

# Envs
arc = os.getenv("ARC")
sts = os.getenv("SITES")
comp = os.getenv("COMP")


@snoop
def yay_check():
    """
    Some of these entries can be commands from
    another package or installed as a dependency
    and not appear, until now, on the 'yay' lists.
    We're going to ask 'yay' to whom do the remaining
    files/apps belong to.
    """
    with open("../../epoch.bin", "rb") as f:
        epoch = pickle.load(f)
    with open(f"{sts}/epoch_counting/left.bin", "rb") as f:
        left = pickle.load(f)

    left_names = [i[0] for i in left if i != i[-1]]

    cmd = "yay -Qo "
    for n in left_names:
        os.system(f"{cmd}{n} >> owners.txt")
    with open("owners.txt", "r") as f:
        own = f.readlines()
    split = [i.split(" ") for i in own]
    clean = [g for g in split if g != g[1]]
    print(clean)


if __name__ == "__main__":
    yay_check()


# @snoop
def names_preparation():
    """
    We'll use the names in the binaries
    produced by 'link_analysis' and:
    1 - Delete repeats,
    2 - Take out slashes and points and
        replace them with underscores.
    If 'link_analysis' is '[]', we'll call
    'epilogue' and end the process.
    """
    with open(f"{arc}finalized.bin", "rb") as f:
        final = pickle.load(f)

    if final != []:
        # Scrapy's spider's can not have slashes or pucntuation marks
        # in them. We take them out here.
        noslashes = [(i[0], i[0].replace("-", "_"), i[1]) for i in final]
        nodots = [(i[0], i[1].replace(".", "_"), i[2]) for i in noslashes]
        spiders = [(i[0], f"{i[1]}_spider", i[2]) for i in nodots]

        # In the 50-100 cohort there were apps that, either were commands of apps
        # that have a manpage or links to pages that are not html. we take them
        # ou here.
        rejects = [
            "disable-paste",
            "mozcerts-qt5",
            "bottle.py",
            "nl-cls-add",
            "nl-route-add",
            "substrings.pl",
            "pamtosrf",
        ]
        sp = [i for i in spiders if i[0] not in rejects]
        with open(f"{arc}spiders.bin", "wb") as f:
            pickle.dump(sp, f)

        return "y"
    else:
        with open(f"{comp}epoch.bin", "rb") as g:
            epoch = pickle.load(g)

        fn = f"{arc}final_data_{epoch[0]}_{epoch[1]}.bin"
        fn_content = []

        with open(fn, "wb") as h:
            pickle.dump(fn_content, h)

        epoch_counting_info()
        delete_files()


# if __name__ == "__main__":
#     names_preparation()
