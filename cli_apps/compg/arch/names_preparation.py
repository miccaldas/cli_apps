"""
Module to prepare the file that'll house
all information entries to use on the
Scrapy project.
"""
import os
import pickle
import shutil

import snoop
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])
load_dotenv()

# Envs
comp = os.getenv("COMP")


@snoop
def yay_check_for_packages():
    """
    Some of these entries can be commands from
    another package or installed as a dependency
    and not appear, until now, on the 'yay' lists.
    We're going to ask 'yay' to whom do the remaining
    files/apps belong to.
    """
    with open("epoch.bin", "rb") as f:
        epoch = pickle.load(f)

    # USE THIS IF STARTING AN EPOCH
    with open(f"{comp}app_data/{epoch[0]}_{epoch[1]}.bin", "rb") as y:
        lft = pickle.load(y)
    # USE THIS IF YOU'RE INSIDE AN EPOCH
    # with open(f"{sts}/epoch_counting/left.bin", "rb") as f:
    #     left = pickle.load(f)
    lft.pop(-1)
    # To work with 'yay' we just need the app's names. We create
    # a list just with them, to ease processing.
    left_names = [i[0] for i in lft]

    # # This commands searches for the package that's the owner of
    # # a given file.
    cmd = "yay -Qo "
    # # We run the remaining names through the 'yay' command, and
    # # send the output to a file.
    # # The first file is for the results, the second for stderr,
    # # because there'll be there the names of the app's it can't
    # # find.
    for n in left_names:
        os.system(f"{cmd}{n} >> owners.txt 2>> notfound.txt")

    with open("owners.txt", "r") as f:
        own = f.readlines()
    # 'own' is a list of strings that look like this.
    # We're going to dplit it in words, and choose only what
    # we want.
    split = [i.split(" ") for i in own]
    # This produces a list in this format:
    # ['/usr/bin/mozcerts-qt5', 'is', 'owned', 'by', 'qca-qt5', '2.3.7-1\n']
    # We just want the string at index[0], part of it, and index[4].

    clean = []
    names = []
    # This loop would dutifully collect all app and package names, but it would
    # do it as many times as there where lists in split. To stop it after
    # completion of full loop, we create a another list that houses the names of
    # the app's already processed. It only runs if the app's name is not there.
    for t in split:
        if t[0] not in names:
            names.append(t[0])
            clean.append([t[0], t[4]])

    with open("yay_packages.bin", "wb") as g:
        pickle.dump(clean, g)


# if __name__ == "__main__":
#     yay_check_for_packages()


# @snoop
def yay_get_package_information():
    """
    We'll get information on the packages
    that own our apps/commands, to see if
    they have information regarding them.
    """
    with open("yay_packages.bin", "rb") as f:
        packs = pickle.load(f)

    pack_names = [[i[0][9:], i[1]] for i in packs]
    with open("file_pack.bin", "wb") as q:
        pickle.dump(pack_names, q)

    for p in pack_names:
        cmd = f"yay -Qi {p[1]} >> package_information.txt"
        os.system(f"{cmd}")


# if __name__ == "__main__":
#     yay_get_package_information()


# @snoop
def names_preparation():
    """
    We'll look through the list of file owners
    and ask 'yay' for information on them. If
    hey look promising, we'll call their info,
    with 'yay -Qi', andkeep only the essential
    data to make a spider and fill the db's
    columns.
    """
    with open("package_information.txt", "r") as g:
        packages = g.readlines()
    if packages != []:
        # We'll divide the output in a sublist per each entry and keep only the name, description and the url. In principle we're
        # not going to use this description value, but something more adequate. But you neveer know.
        packs_lst = []
        temp = []
        for i in packages:
            if i == "\n":
                temp.append(i)
                packs_lst.append(temp)
                temp = []
            else:
                temp.append(i)

        # This loop was repeating the information has many times as it has sublists. The 'names' if clause stops it.
        short_info = []
        names = []
        for sub in packs_lst:
            if sub[0] not in names:
                names.append(sub[0])
                short_info.append([sub[0][18:], sub[2][18:], sub[4][18:]])

        cln = [[i.strip() for i in sub] for sub in short_info]

        with open("file_pack.bin", "rb") as q:
            fp = pickle.load(q)

        clean = [i + [t[0]] for i in cln for t in fp if i[0] == t[1]]
        with open("entries.bin", "wb") as f:
            pickle.dump(clean, f)

        return "y"


if __name__ == "__main__":
    names_preparation()
