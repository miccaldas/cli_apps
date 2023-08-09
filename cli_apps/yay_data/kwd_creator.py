"""
Keyword creator for *Arch* packages.
Runs KeyBERT, to find keywords for each package.
Stores them in a file in the *kws* folder.
"""
import pickle

# import snoop
from keybert import KeyBERT

# from snoop import pp
from thefuzz import fuzz, process


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def kwd_creator():
    """
    We run KeyBERT through *newnames.bin*.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags/"

    with open("newnames.bin", "rb") as f:
        nn = pickle.load(f)

    for tup in nn:
        name = tup[0]
        text = tup[1]
        badwords = [f"{name}", "codespace", "codespaces", "svn", "pypi"]
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
                # If there's a reasonable index of disimilarity:
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
    kwd_creator()
