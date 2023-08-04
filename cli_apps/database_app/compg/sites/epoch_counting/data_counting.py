"""
Temporary module to control what is done
and what it still needs to be done in
each epoch.
"""
import os
import pickle

# import snoop
from cli_apps.database_app.methods import print_template
from dotenv import load_dotenv
from rich import print as rprint
from snoop import pp

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])

load_dotenv()
# Envs
scr = os.getenv("SITES")
comp = os.getenv("COMP")
app = os.getenv("APPDATA")


# @snoop
def data_counting():
    """"""
    with open(f"{comp}epoch.bin", "rb") as f:
        epoch = pickle.load(f)
    low = epoch[0]
    high = epoch[1]

    filename = f"{app}/{low}_{high}.bin"
    with open(filename, "rb") as g:
        ur = pickle.load(g)

    cwd = f"{scr}/epoch_counting/"
    filelst = os.listdir(cwd)

    # We take out the '_data.bin' prefix of the data files, to get
    # their site's names.
    processed = [y[:-9] for y in filelst if y.endswith("data.bin")]

    datas = []
    # 'datas' will gather the name of the site and the list of processed
    # apps in a tuple. If the list of processed is 0, the name will serve
    # to build a warning message. The lists will be joined and, the apps
    # within will be subtracted to cohort's original list, to create a
    # updated 'left' file.
    for i in processed:
        if i.startswith("command"):
            with open(f"{cwd}command_linux_data.bin", "rb") as h:
                cmd = pickle.load(h)
                datas.append((i, cmd))
        if i.startswith("gthb"):
            with open(f"{cwd}gthb_data.bin", "rb") as y:
                git = pickle.load(y)
                git = []
                datas.append((i, git))
        if i.startswith("linux"):
            with open(f"{cwd}linux_die_data.bin", "rb") as j:
                die = pickle.load(j)
                datas.append((i, die))
        if i.startswith("pypi"):
            with open(f"{cwd}pypi_data.bin", "rb") as m:
                pip = pickle.load(m)
                datas.append((i, pip))
        if i.startswith("debian"):
            with open(f"{cwd}debian_manpage_data.bin", "rb") as n:
                deb = pickle.load(n)
                datas.append((i, deb))
        if i.startswith("gnu"):
            with open(f"{cwd}gnu_ftp_data.bin", "rb") as o:
                gnu = pickle.load(o)
                datas.append((i, gnu))
        if i.startswith("man7"):
            with open(f"{cwd}man7_data.bin", "rb") as p:
                mn7 = pickle.load(p)
            datas.append((i, mn7))
        if i.startswith("source"):
            with open(f"{cwd}sourceware_data.bin", "rb") as q:
                src = pickle.load(q)
                datas.append((i, src))
        if i.startswith("help"):
            with open(f"{cwd}helpmanual_data.bin", "rb") as r:
                hlp = pickle.load(r)
                datas.append((i, hlp))
        if i.startswith("mixed"):
            with open(f"{cwd}mixed_data.bin", "rb") as s:
                mix = pickle.load(s)
                datas.append((i, mix))

    # We'll look for data files that output '[]'. That means that
    # they found nothing in this cohort for their site. We output
    # a warning message ad delete their entry from 'datas'.
    for t in datas:
        if t[1] == []:
            print_template(
                f"{t[0]}'s output for the {low}-{high} epoch was 0.",
                "bold #F31559\n",
            )
            datas.remove(t)
    # The any clause returns 'True' if at least one of the elements of the iterable is true.
    # Here it was an expedient way to put this separator below the above loop, avoiding creating another.
    if any(t[1] == [] for t in datas):
        rprint(
            "[bold #FFDBAA]          //////////////////////////////////////////////////////////"
        )

    # We collect the processed app's names. As we, depending on the site,
    # receive data in list of lists or list of dictionaries format, we
    # have two modes of collection.
    names = []
    for d in datas:
        for sub in d[1]:
            if type(sub) == list or type(sub) == tuple:
                names.append(sub[0])
            if type(sub) == dict:
                names.append(sub["name"])

    # These were apps that we discarded for one reason or another, We have to account for them.
    tk = [
        "mutevolume.sh",
        "signonpluginprocess",
        "disable-paste",
        "rst2latex.py",
        "scrape",
        "bottle.py",
        "flask",
        "scrapy",
        "nl-cls-add",
        "nl-route-add",
        "jps",
    ]
    names += tk
    # 'left' is a file that has an updated number of app's to process in cohort.
    left = [u for u in ur if u[0] not in names]
    with open("left.bin", "wb") as t:
        pickle.dump(left, t)

    # Function's output.
    # Two things of note:
    # 1 - Don't put '[/]' before declaring a new style. Not needed.
    # 2 - If you have a style inserted in another, to terminate it
    #     don't write '[/]', it won't work. Write '[/<style_definition>]'.
    #     See the second print_template() call as an example.
    rprint(
        "[bold #FFDBAA]          //////////////////////////////////////////////////////////"
    )
    print_template(f"The epoch is[bold #FFC6AC] {epoch}")
    print_template(
        f"There's [bold #FFC6AC]{len(left)}[/bold #FFC6AC] apps to process in this epoch"
    )
    print_template(f"The site's already processed are [bold #FFC6AC]{processed}")


if __name__ == "__main__":
    data_counting()
