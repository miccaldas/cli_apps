"""
Keyword creator for *Arch* packages.
Cleans bin file data and runs KeyBERT,
to find keywords for each package.
"""
import os
import pickle
import re
import subprocess
import sys

import snoop
from cli_apps.database_app.methods import input_decision, print_template
from dotenv import load_dotenv
from keybert import KeyBERT

# from snoop import pp
from thefuzz import fuzz, process


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()

# Envs
mix = os.getenv("MIX")
project = os.getenv("MIXPROJ")


@snoop
def universal_objects():
    """
    Collects and defines variables and
    python objects that will be used by
    several functions.
    """
    with open("finalized.bin", "rb") as g:
        cleandata = pickle.load(g)
    with open(f"{project}results.bin", "rb") as f:
        entries = []
        while True:
            try:
                entries.append(pickle.load(f))
            except EOFError:
                break

    return cleandata, entries


@snoop
def ubuntu_cleaner():
    """
    Cleans entries in 'results.bin' that come from 'Ubuntu' manpages.
    """
    objs = universal_objects()
    cleandata = objs[0]
    entries = objs[1]

    # In the spiders we've created commands generally expecting that we have a generalist 'response.css'
    # that'll gather info from most sites, another for 'github', and another for 'sourceforge'. We'll
    # split 'entries in these 3 groups.'
    # for c in cleandata:
    #     if c[2].startswith("https://manpages.ubuntu.com/"):
    #         ubuntus.append(c)
    ub = [c[0] for c in cleandata if c[1].startswith("https://manpages.ubuntu.com")]
    ubuntus = [e for e in entries if e["name"] in ub]

    # Some entries have a name with a '.py' prefix, that isn't used wsed when reffering to the app in the
    # 'ubuntus' response.css() results. Because later on we'll be veryfying if a string starting with the
    # name exists in 'ubuntus', we have to make sure that they're equal on both sides.
    [
        u.update({"name": f'{u["name"][:-3]}'})
        for u in ubuntus
        if u["name"].endswith(".py")
    ]

    # We find lines that start with '[name] - '. They have a very short description after the dash that we
    # want to use for the 'presentation' field and as text for 'kwd_creator'.
    lines = []
    for u in ubuntus:
        for line in u["ubuntus"]:
            # One entry uses a slightly bigger dash character than the others. We create an option for that.
            if line.find(f"{u['name']} - ") != -1 or line.find(f"{u['name']} — ") != -1:
                lines.append(line)
                break

    # By spliting the lines gathered in the loop above, we create lists that have the app name and the
    # 'presentation' value as elements. We collect them all in another list.
    line_lists = []
    for line in lines:
        if " - " in line:
            lnlst = line.split(" - ")
            line_lists.append(lnlst)
        if " — " in line:
            lnlst = line.split(" — ")
            line_lists.append(lnlst)

    # We strip the lists elements of linebreaks and empty spaces.
    ubuntulines = []
    for lst in line_lists:
        clst = [lst[0].strip(), lst[1].strip()]
        ubuntulines.append(clst)

    return ubuntulines


@snoop
def sourceforge_cleaner():
    """
    Cleans entries coming from Sourceforge.
    """
    objs = universal_objects()
    entries = objs[1]

    # TODO: Automate the collection of entries with results through 'sourceforge' response.css()
    sf = ["pbmtonokia"]
    srcfrg = [e for e in entries if e["name"] in sf]

    srclines = []
    for s in srcfrg:
        s.update({"sourceforge": [i.strip() for i in s["sourceforge"]]})
        srclines.append([s["name"], s["sourceforge"][0]])

    return srclines


@snoop
def generic_cleaner():
    """
    Cleans all entries not coming
    from Github or Sourceforge.
    """
    objs = universal_objects()
    cleandata = objs[0]
    entries = objs[1]

    ubs = ubuntu_cleaner()
    sfs = sourceforge_cleaner()

    ub = [u[0] for u in ubs]
    sf = [s[0] for s in sfs]

    ub_sf = ub + sf
    gens = [e for e in entries if e["name"] not in ub_sf]
    gene = [
        g
        for g in gens
        if g["name"] != "rst2latex.py"
        and g["name"] != "fh2svg"
        and "rst2man.py" != g["name"]
    ]
    genes = [[r["name"], r["content"]] for r in gene if r["content"] != []]
    gener = [[sub[0], [v.strip() for v in sub[1]]] for sub in genes]

    empties = [[sub[0], [v for v in sub[1] if v != ""]] for sub in gener]
    comma = [[sub[0], [v for v in sub[1] if v != ","]] for sub in empties]
    commaspace = [[sub[0], [v for v in sub[1] if v != ", "]] for sub in comma]
    point = [[sub[0], [v for v in sub[1] if v != "."]] for sub in commaspace]

    # In 'point' there's entries we can get the 'presentation' value from the first
    # item from content, and some that do not. We'll seprate them in two different lists.
    # This first list are those that we cannot take the 'presentation' value in the first line.
    nofirst = [
        "vboximg-mount",
        "ppmtospu",
        "sst_dump",
        "qmlimportscanner-qt5",
        "vboximg-mount",
        "vss2xhtml",
    ]
    firsts = [p for p in point if p[0] not in nofirst]

    # As there was no way to create a method, shareable by all, that would get a good 'presentation'
    # value, we'll do it by hand.
    seconds = [
        ["vss2xhtml", "Converts Microsoft Visio stencils to SVG."],
        [
            "ppmtospu",
            "This program converts from the PPM format to the uncompressed Spectrum 512 image format usedon Atari ST computers.",
        ],
        [
            "sst_dump",
            "sst_dump tool can be used to gain insights about a specific SST file.",
        ],
        [
            "qmlimportscanner-qt5",
            "Runs at configure time to find the static QML plugins used and links them to the given target.",
        ],
        [
            "vboximg-mount",
            "Command line utility for Mac OS X hosts that provides raw access to an Oracle VM VirtualBox virtual disk image on the host system",
        ],
    ]

    genericlns = [[f[0], f[1][0]] for f in firsts]
    genericlns += seconds
    genericlines = [[i.replace("\n", " ") for i in sub] for sub in genericlns]

    return genericlines


@snoop
def final_list():
    """"""
    uni = universal_objects()
    cleandata = uni[0]

    ulines = ubuntu_cleaner()
    slines = sourceforge_cleaner()
    glines = generic_cleaner()
    flines = ulines + slines + glines

    [i.append(f[1]) for i in flines for f in cleandata if i[0] == f[0]]

    with open(f"{mix}clean_list.bin", "wb") as f:
        pickle.dump(flines, f)


if __name__ == "__main__":
    final_list()


@snoop
def kwd_creator():
    """
    We run KeyBERT through *clean_list.bin*.
    I chose to make the changes to the data
    still in the spider, so I don't have need
    for the 'bin_cleaner' module. I'll keep it
    commented, because we don't know if I'll
    change my mind again.
    """
    filelst = os.listdir(f"{mix}")

    if "clean_list.bin" in filelst:
        with open(f"{mix}/clean_list.bin", "rb") as f:
            content = pickle.load(f)
        print_template(
            f"Using [bold #FFC6AC]clean_list.bin[/bold #FFC6AC] file found in {mix}"
        )
    else:
        with open(f"{project}results.bin", "rb") as g:
            content = []
            while True:
                try:
                    content.append(pickle.load(g))
                except EOFError:
                    break
        print_template(
            f"Using [bold #FFC6AC]results.bin[/bold #FFC6AC] file from {project}"
        )

    print_template(f"{content}")
    print("\n")
    desc_decision = input_decision("[+] - Do you want to continue?[y/n]")
    if desc_decision == "n":
        raise SystemExit

    if all(type(i) == tuple for i in content):
        txts = [(i[0], i[2]) for i in content]
    if all(type(i) == list for i in content):
        txts = [(i[0], i[1]) for i in content]
    if all(type(i) == dict for i in content):
        txts = []
        for dic in content:
            temp = []
            name = dic["name"]
            for c in dic["content"]:
                # 'content' has a prefix with the app's name the we don't want to be
                # in text, because we're going to expressly insert it as the first tag.
                if c.startswith(f"{name}: - "):
                    txt = c.split(" - ")[1]
                    temp.append(txt)
                else:
                    temp.append(c)
            txts.append(temp)

    for t in txts:
        name = t[0]
        text = t[1]
        badwords = ["codespace", f"{name}", "format"]
        kw_model = KeyBERT()
        keys = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 1),
            stop_words=badwords,
        )
        keywords = [o for o, p in keys]
        kwds = []
        # This is here to ensure that the keywords are not very similar.
        for y in keywords:
            # Create a list without one of the keywords.
            slst = [b for b in keywords if b != y]
            # If the keyword list is greater than one:
            if slst != []:
                # We compare the similarity index of the keyword against
                # all of the others.
                value = process.extractOne(y, slst)
                # If there's a resonable index of disimilarity:
                if value[1] < 85:
                    # keep the keyword.
                    kwds.append(y)
        # List of keywords that weren't chosen in the latter process.
        similars = [u for u in keywords if u not in kwds]
        # If the list is not empty:
        if similars != []:
            # get the longest keyword in there:
            sim_choice = max(similars, key=len)
            # and add it to the chosen keywords list.
            kwds += [sim_choice]

        with open(f"{mix}kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()
