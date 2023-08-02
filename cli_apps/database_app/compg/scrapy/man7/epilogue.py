"""
Module Docstring
"""
import os
import pickle
import shutil

# import snoop
from cli_apps.database_app.compg.scrapy.epoch_counting.data_counting import (
    data_counting,
)
from cli_apps.database_app.methods import print_template
from dotenv import load_dotenv

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])

load_dotenv()
# Envs
mn7 = os.getenv("MN7")
comp = os.getenv("COMP")
scrapy = os.getenv("SCRAPY")


# @snoop
def universal_variables():
    """
    Defines and returns a series of variables
    the other functions can use.
    """
    with open(f"{comp}epoch.bin", "rb") as i:
        epoch = pickle.load(i)

    fd = f"{mn7}final_data_{epoch[0]}_{epoch[1]}.bin"
    epoch_file = f"{mn7}man7_data.bin"
    ini = f"{mn7}urls_{epoch[0]}_{epoch[1]}.bin"
    bins = f"{mn7}binaries/"

    return fd, epoch_file, ini, bins, epoch[0], epoch[1]


# @snoop
def epoch_counting_info():
    """
    This block deals with sending information to
    'epoch_counting'. We have a try/except code
    to stop the function in case something goes wrong
    in this critical stage.
    """
    vr = universal_variables()

    shutil.copy(vr[0], vr[1])
    try:
        shutil.move(vr[1], f"{scrapy}epoch_counting/")
    except FileNotFoundError as e:
        print_template(f"Couldn't move {mn7.split('/')[-1]}mn7_data.bin because of:\n[bold #F31559]{e}")
        raise SystemExit
    data_counting()


if __name__ == "__main__":
    epoch_counting_info()


# @snoop
def copy_files():
    """
    Copying some files to 'binaries'. The folder is meant
    as an archive to store information we may reffer to
    on a later data.
    """
    vr = universal_variables()

    try:
        cmd1 = shutil.copy(vr[0], vr[3])
        cmd2 = shutil.copy(vr[2], vr[3])
    except (FileNotFoundError, IOError) as e:
        print_template(f"A copy command has failed with error:\n[bold #F31559]{e}")
        return "n"
        raise SystemExit
    return "y"


# @snoop
def delete_files():
    """
    This block is dedicated to trashing files. We're using
    'trash-put', because the deleted files are retrievable.
    """
    vr = universal_variables()
    cp = copy_files()

    if cp == "y":
        filelst = os.listdir(f"{mn7}")
        files = [
            "clean_list.bin",
            "clean_data.bin",
            "helpmanual_data.bin" "finalized.bin",
            "left.bin",
            "spiders.bin",
            f"urls_{vr[4]}_{vr[5]}.bin",
            f"final_data_{vr[4]}_{vr[5]}.bin",
        ]
        cmd = "/usr/bin/trash-put "
        flst = [i for i in filelst if i in files]
        for i in flst:
            os.system(f"{cmd}{mn7}{i}")


if __name__ == "__main__":
    delete_files()
