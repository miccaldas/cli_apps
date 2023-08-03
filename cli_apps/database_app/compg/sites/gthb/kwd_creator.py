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
from dotenv import load_dotenv
from keybert import KeyBERT

# from snoop import pp
from thefuzz import fuzz, process


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()

# Envs
git = os.getenv("GIT")
project = os.getenv("GITPROJ")


# @snoop
def bin_cleaner():
    """
    Binary cleaner.
    We remove html tags, linebreaks, exccess whitespaces from the scraped content.
    """

    lines = []
    with open(f"{project}results.bin", "rb") as f:
        entries = []
        while True:
            try:
                entries.append(pickle.load(f))
            except EOFError:
                break

    clean_list = []
    for i, t in enumerate(entries):
        lst = entries[i]["content"]
        lt = [i.replace("<i>", "").replace("</i>", "").replace("</a>", "") for i in lst]
        lt.pop(-1)
        llt = [re.sub('<a href=.+">', "", i) for i in lt]
        clean_list.append(llt)
    with open(f"{git}clean_list.bin", "wb") as f:
        pickle.dump(clean_list, f)


if __name__ == "__main__":
    bin_cleaner()


# @snoop
def kwd_creator():
    """
    We run KeyBERT through *clean_list.bin*.
    """
    with open(f"{git}/clean_list.bin", "rb") as f:
        str_content = pickle.load(f)

    # We turn the list of strings into one string, so keyBERT can read it.
    content = [[" ".join(lst)] for lst in str_content]

    for lst in content:
        name = lst[0].split(" - ")[0]
        text = lst[0].split(" - ")[1]

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

        with open(f"{git}/kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()
