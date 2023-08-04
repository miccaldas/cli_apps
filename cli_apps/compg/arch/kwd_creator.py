"""
Keyword creator for *Arch* packages.
"""
import os
import pickle
import re
import subprocess
import sys

import snoop
from cli_apps.database_app.methods import input_decision, print_template
from db import dbdata
from keybert import KeyBERT
from snoop import pp
from thefuzz import fuzz, process


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def entries_db_comparison():
    """
    We'll check for what is alreasy in the db.
    """
    with open("entries.bin", "rb") as f:
        content = pickle.load(f)

    query = "SELECT name FROM cli_apps"
    dbnms = dbdata(query, "fetch")
    dbnames = [i for sub in dbnms for i in sub]
    db_cull = [i for i in content if i[0] not in dbnames]

    with open("db_cull.bin", "wb") as g:
        pickle.dump(db_cull, g)


@snoop
def kwd_creator():
    """
    We run KeyBERT through *entries.bin*.
    """
    filelst = os.listdir(f"{os.getcwd()}")

    # if "entries.bin" in filelst:
    #     with open(f"{arc}/entries.bin", "rb") as f:
    #         content = pickle.load(f)
    # else:
    #     print_template("[bold #F31559]Can't find the 'entries.bin' file.")
    #     print("\n")
    with open("db_cull.bin", "rb") as f:
        content = pickle.load(f)
    print_template(f"{content}")
    print("\n")
    desc_decision = input_decision("[+] - Do you want to continue?[y/n]")
    if desc_decision == "n":
        raise SystemExit

    txts = [(i[-1], i[1]) for i in content]

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

        with open(f"kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    # entries_db_comparison()
    kwd_creator()
