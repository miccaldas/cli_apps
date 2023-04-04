"""
Cleans csv file data and runs KeyBERT, to find keywords for each package.
Stores them in a file in the *kwds* folder.
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
    The column names were repeated for each entry, we remove them here.
    We remove also the excess whitespaces from the scraped content.
    """
    cwd = os.getcwd()
    pth = f"{cwd}/yay_project/"

    lines = []
    with open(f"{pth}/results.csv", "r") as f:
        reader = csv.reader(f)
        for line in reader:
            lines.append(line)

    content = [i for i in lines if i != ["name", "content"]]

    nospaces = []
    for k in range(len(content)):
        x = re.sub("\s+", " ", content[k][1])
        nospaces.append([content[k][0], x])
    with open("nospaces.bin", "wb") as t:
        pickle.dump(nospaces, t)


if __name__ == "__main__":
    csv_cleaner()


@snoop
def kwd_creator():
    """
    We run KeyBERT through the csv results, this time without a stop_word list.\n
    It was much faster and the results aren't worst because of it.\n
    .. NOTE::
        This turned out to be completely wrong. Keybert created a lot of keywords
        equal to the package name. But we already have that in *t1*.
    """
    with open("nospaces.bin", "rb") as f:
        csvcontent = pickle.load(f)

    for line in csvcontent:
        name = line[0]
        text = line[1]
        kw_model = KeyBERT()
        keys = kw_model.extract_keywords(
            text,
            keyphrase_ngram_range=(1, 1),
            stop_words="english",
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
        with open(f"kwds/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()
