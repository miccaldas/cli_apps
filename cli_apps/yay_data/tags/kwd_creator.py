"""
Keyword creator for *Arch* packages.
Cleans csv file data and runs KeyBERT, to find keywords for each package.
Stores them in a file in the *kws* folder.
"""
import csv
import os
import pickle
import re
import subprocess

import snoop
from keybert import KeyBERT
from snoop import pp
from thefuzz import fuzz, process


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def csv_cleaner():
    """
    Csv cleaner for *Arch* packages.
    We remove column names and the exccess whitespaces from the scraped content.
    """
    cwd = os.getcwd()
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"

    lines = []
    with open(f"{tags}/yay_project/results.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            lines.append(line)

    content = [i for i in lines if i != ["name", "content"]]

    nospaces = []
    for k in range(len(content)):
        x = re.sub("\s+", " ", content[k][1])
        nospaces.append([content[k][0], x])
    with open(f"{tags}/nospaces.bin", "wb") as t:
        pickle.dump(nospaces, t)


if __name__ == "__main__":
    csv_cleaner()


@snoop
def kwd_creator():
    """
    We run KeyBERT through *nospaces.bin*.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"

    with open(f"{tags}/nospaces.bin", "rb") as f:
        csvcontent = pickle.load(f)

    for line in csvcontent:
        name = line[0]
        text = line[1]
        badwords = [f"{name}", f"n{name}", "codespace", "codespaces", "svn", "pypi"]
        kw_model = KeyBERT()
        keys = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 1),
            stop_words=badwords,
        )
        keywords = [o for o, p in keys]

        kwds = []
        for y in keywords:
            slst = [b for b in keywords if b != y]
            if slst != []:
                value = process.extractOne(y, slst)
                if value[1] < 85:
                    kwds.append(y)
        similars = [u for u in keywords if u not in kwds]
        if similars != []:
            sim_choice = max(similars, key=len)
            kwds += [sim_choice]
        with open(f"{tags}/kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()
