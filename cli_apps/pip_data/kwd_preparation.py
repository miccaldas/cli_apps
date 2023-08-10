"""
Does all eyword management.
Creates keywords from the 'presentation' fields
in 'newurls.bin' and adds them to the rest of
the information in a file called 'kwdlst.bin'
"""
import os
import pickle

import snoop
from keybert import KeyBERT

# from snoop import pp
from thefuzz import fuzz, process

# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def kwd_creator():
    """
    We run KeyBERT through the 'newurls.bin' results.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data/"

    with open(f"{pip}/newurls.bin", "rb") as f:
        content = pickle.load(f)

    for sub in content:
        name = sub[0]
        text = sub[1]
        badwords = [f"{name}", "codespace", "codespaces", "for"]
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

        with open(f"{pip}/kws/{name}", "w") as v:
            for q in kwds:
                v.write(f"{q}\n")


if __name__ == "__main__":
    kwd_creator()


# @snoop
def kwd_collector():
    """
    Collects the keywords to a new list.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data"
    fldr = "/home/mic/python/cli_apps/cli_apps/pip_data/kws"
    fllst = os.listdir(fldr)
    with open(f"{pip}/newurls.bin", "rb") as y:
        nn = pickle.load(y)

    kwdlst = []
    for file in fllst:
        with open(f"{fldr}/{file}", "r") as f:
            kws = f.readlines()
            if len(kws) >= 3:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = kws[2].strip()
                ndata = [
                    (c[0], c[1], c[2], c[0].lower(), t2, t3, t4, "pip")
                    for c in nn
                    if c[0] == f"{file}"
                ]
                kwdlst.append(ndata)
            if len(kws) == 2:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = "NA"
                ndata = [
                    (c[0], c[1], c[2], c[0].lower(), t2, t3, t4, "pip")
                    for c in nn
                    if c[0] == f"{file}"
                ]
                kwdlst.append(ndata)
            if len(kws) == 1:
                t2 = kws[0].strip()
                t3 = "NA"
                t4 = "NA"
                ndata = [
                    (c[0], c[1], c[2], c[0].lower(), t2, t3, t4, "pip")
                    for c in nn
                    if c[0] == f"{file}"
                ]
                kwdlst.append(ndata)
            if kws == []:
                t2 = "NA"
                t3 = "NA"
                t4 = "NA"
                ndata = [
                    (c[0], c[1], c[2], c[0].lower(), t2, t3, t4, "pip")
                    for c in nn
                    if c[0] == f"{file}"
                ]
                kwdlst.append(ndata)

    with open(f"{pip}/kwdlst.bin", "wb") as f:
        pickle.dump(kwdlst, f)


if __name__ == "__main__":
    kwd_collector()
