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


# if __name__ == "__main__":
#     ubuntu_cleaner()


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
        srclines.append((s["name"], s["sourceforge"][0]))

    return srclines


# if __name__ == "__main__":
#     sourceforge_cleaner()


@snoop
def general_cleaner():
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
    generics = [[sub[0], [v for v in sub[1] if v != ""]] for sub in gener]
    for h in generics:
        print(h)
    # splits = []
    # descs = []
    # # We identified two patterns in the site that give good results.
    # # We'll look for one, if it fails, we'll for the other.
    # for i, t in enumerate(entries):
    #     name = entries[i]["name"]
    #     lst = entries[i]["content"]
    # # We're looking for twothings in 'lst', a quote for the field 'description'
    # # probably the same thing for keyword creation. We've noticed that more text
    # # doesn't mean better results. So, unless we start seeing bad results, the
    # # 'edscription' filed and keyBERT are fed with the same text.
    # for ls in lst:
    #     # We split the content string in the breakline points, to mimic the appearance
    #     # of the web page.
    #     splits = ls.split("\n")
    #     for idx, line in enumerate(splits):
    #         # If line starts with this pattern....
    #         if line.startswith(name + ": - "):
    #             # split on it and keep the second half.
    #             desc = line.split(": - "[1])
    #             descs.append(name, desc)
    #             break
    #         if descs == []:
    #             if line.startswith("Usage: "):
    #                 descs.append((name, splits[i]))

    # desc_decision = input_decision(f"[+] - Descs is [bold #FFC6AC]{descs}[/bold #FFC6AC]. Do you want to continue?[y/n]")
    # if desc_decision == "n":
    #     raise SystemExit

    # # We'll add the text to cleandata, so as to have all found info in the same place.
    # clst = []
    # for desc in descs:
    #     for c in cleandata:
    #         if desc[0] == c[0]:
    #             info = c + (desc[1],)
    #             clst.append(info)

    # with open(f"{mn7}clean_list.bin", "wb") as f:
    #     pickle.dump(clst, f)


if __name__ == "__main__":
    general_cleaner()


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

    print(content)
    desc_decision = input_decision("[+] - Do you want to continue?[y/n]")
    if desc_decision == "n":
        raise SystemExit

    if all(type(i) == tuple for i in content):
        txts = [(i[0], i[2]) for i in content]
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


# if __name__ == "__main__":
#     kwd_creator()
