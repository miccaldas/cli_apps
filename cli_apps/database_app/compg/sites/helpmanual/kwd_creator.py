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
hlp = os.getenv("HLP")
project = os.getenv("HLPPROJ")


@snoop
def bin_cleaner():
    """
    Binary cleaner. This function remains, and probably
    will for a while, very protean. As page struture change,
    so must the cleaning. Commented are kept things that
    worked for some situations but may not work for others.
    Until we're  very secure on the page structure on this
    site, will have to be tentative.
    """
    with open("finalized.bin", "rb") as g:
        cleandata = pickle.load(g)
    lines = []
    with open(f"{project}results.bin", "rb") as f:
        entries = []
        while True:
            try:
                entries.append(pickle.load(f))
            except EOFError:
                break

    splits = []
    descs = []
    # We identified two patterns in the site that give good results.
    # We'll look for one, if it fails, we'll for the other.
    for i, t in enumerate(entries):
        name = entries[i]["name"]
        lst = entries[i]["content"]
    # We're looking for twothings in 'lst', a quote for the field 'description'
    # probably the same thing for keyword creation. We've noticed that more text
    # doesn't mean better results. So, unless we start seeing bad results, the
    # 'edscription' filed and keyBERT are fed with the same text.
    for ls in lst:
        # We split the content string in the breakline points, to mimic the appearance
        # of the web page.
        splits = ls.split("\n")
        for idx, line in enumerate(splits):
            # If line starts with this pattern....
            if line.startswith(name + ": - "):
                # split on it and keep the second half.
                desc = line.split(": - "[1])
                descs.append(name, desc)
                break
            if descs == []:
                if line.startswith("Usage: "):
                    descs.append((name, splits[i]))

    desc_decision = input_decision(f"[+] - Descs is {descs}. Do you want to continue?[y/n]")
    if desc_decision == "n":
        raise SystemExit

    # We'll add the text to cleandata, so as to have all found info in the same place.
    clst = []
    for desc in descs:
        for c in cleandata:
            if desc[0] == c[0]:
                info = c + (desc[1],)
                clst.append(info)

    with open(f"{hlp}clean_list.bin", "wb") as f:
        pickle.dump(clst, f)


# if __name__ == "__main__":
#     bin_cleaner()


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
    filelst = os.listdir(f"{hlp}")

    if "clean_list.bin" in filelst:
        with open(f"{hlp}/clean_list.bin", "rb") as f:
            content = pickle.load(f)
        print_template(f"Using clean_list.bin file found in {hlp}")
    else:
        with open(f"{project}results.bin", "rb") as g:
            content = []
            while True:
                try:
                    content.append(pickle.load(g))
                except EOFError:
                    break
        print_template(f"Using results.bin from {project}")

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

        with open(f"{hlp}kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()
