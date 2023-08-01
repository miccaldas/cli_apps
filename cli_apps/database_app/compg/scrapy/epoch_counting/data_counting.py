"""
Temporary module to control what is done
and what it still needs to be done in
each epoch.
"""
import os
import pickle

from cli_apps.database_app.methods import print_template
from dotenv import load_dotenv

# import snoop


# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])

load_dotenv()
# Envs
scr = os.getenv("SCRAPY")
comp = os.getenv("COMP")


# @snoop
def data_counting():
    """"""
    with open(f"{comp}epoch.bin", "rb") as f:
        epoch = pickle.load(f)
    low = epoch[0]
    high = epoch[1]
    filename = f"{comp}app_data/{low}_{high}.bin"
    with open(filename, "rb") as g:
        ur = pickle.load(g)

    cwd = f"{scr}/epoch_counting/"

    processed = ["command_linux", "gthb", "linux_die", "pypi", "debian_manpage"]

    with open(f"{cwd}command_linux_data.bin", "rb") as h:
        cmd = pickle.load(h)
    with open(f"{cwd}gthb_data.bin", "rb") as i:
        git = pickle.load(i)
    git = []
    with open(f"{cwd}linux_die_data.bin", "rb") as j:
        die = pickle.load(j)
    with open(f"{cwd}pypi_data.bin", "rb") as m:
        pip = pickle.load(m)
    with open(f"{cwd}debian_manpage_data.bin", "rb") as n:
        hlp = pickle.load(n)

    # print("command")
    # print(cmd)
    # print("\n")
    # print("gthb")
    # print(git)
    # print("\n")
    # print("linux-die")
    # print(die)
    # print("\n")
    # print("pypi")
    # print(pip)
    # print("\n")

    names = []

    datas = [cmd, die, pip, hlp]
    for i, t in enumerate(datas):
        for sub in t:
            if type(sub) == list:
                names.append(sub[0])
            if type(sub) == dict:
                names.append(sub["name"])

    left = [u for u in ur if u[0] not in names]
    with open("left.bin", "wb") as t:
        pickle.dump(left, t)

    print_template(f"The epoch is {epoch}")
    print_template(f"There's {len(left)} apps to process in this epoch")
    print_template(f"The site's already processed are {processed}")


if __name__ == "__main__":
    data_counting()
