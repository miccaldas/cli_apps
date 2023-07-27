"""
Keyword creator for Pip packages.
Cleans csv file data and runs KeyBERT, to find keywords for each package.
Stores them in a file in the *kws* folder.
"""
import csv
import os
import pickle
import re
import subprocess
import sys

# import snoop
from keybert import KeyBERT

# from snoop import pp
from thefuzz import fuzz, process

# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def csv_cleaner():
    """
    Csv cleaner for Pip packages.
    We remove column names and also the exccess whitespaces from the scraped content.
    """
    pth = "/home/mic/python/cli_apps/cli_apps/pip_data/pip_project"
    csv.field_size_limit(sys.maxsize)
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
    with open("/home/mic/python/cli_apps/cli_apps/pip_data/tags/nospaces.bin", "wb") as t:
        pickle.dump(nospaces, t)


if __name__ == "__main__":
    csv_cleaner()


# @snoop
def kwd_creator():
    """
    We run KeyBERT through the csv results.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/pip_data/tags"

    with open(f"{tags}/nospaces.bin", "rb") as f:
        csvcontent = pickle.load(f)

    for line in csvcontent:
        name = line[0]
        text = line[1]
        badwords = [f"{name}", f"n{name}", "codespace", "codespaces"]
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

        with open(f"{tags}/kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()
