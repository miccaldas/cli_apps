"""
Module to prepare the file that'll house
all information entries to use on the
Scrapy project.
"""
import os
import pickle
import shutil

# import snoop
from cli_apps.database_app.compg.link_analysis import url_searcher
from dotenv import load_dotenv
from snoop import pp

from epilogue import copy_files, delete_files, epoch_counting_info

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
# load_dotenv()

# Envs
mn7 = os.getenv("MN7")
scr = os.getenv("SCRAPY")
comp = os.getenv("COMP")


# @snoop
def call_analysis():
    """
    Calls 'url_searcher'.
    """
    with open("../../epoch.bin", "rb") as f:
        epoch = pickle.load(f)

    url_searcher("https://man7.org", f"{scr}/epoch_counting/left.bin")
    shutil.copy(f"{mn7}urls_{epoch[0]}_{epoch[1]}.bin", f"{mn7}finalized.bin")


# if __name__ == "__main__":
#     call_analysis()


# @snoop()
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
    with open(f"{mn7}finalized.bin", "rb") as f:
        final = pickle.load(f)

    if final != []:
        # Scrapy's spider's can not have slashes or pucntuation marks
        # in them. We take them out here.
        noslashes = [(i[0], i[0].replace("-", "_"), i[1]) for i in final]
        nodots = [(i[0], i[1].replace(".", "_"), i[2]) for i in noslashes]
        spiders = [(i[0], f"{i[1]}_spider", i[2]) for i in nodots]

        with open(f"{mn7}spiders.bin", "wb") as f:
            pickle.dump(spiders, f)

        return "y"
    else:
        with open(f"{comp}epoch.bin", "rb") as g:
            epoch = pickle.load(g)

        fn = f"{mn7}final_data_{epoch[0]}_{epoch[1]}.bin"
        fn_content = []

        with open(fn, "wb") as h:
            pickle.dump(fn_content, h)

        epoch_counting_info()
        delete_files()


if __name__ == "__main__":
    names_preparation()
