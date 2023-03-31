"""
Analyzes the content of ''
"""
import csv
import os
import string

import snoop
import yake
from snoop import pp
from thefuzz import fuzz, process

# import subprocess


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def kwd_creator():
    """"""

    cwd = os.getcwd()

    projlst = os.listdir(cwd)
    proj_lst = [w for w in projlst if w.endswith("_project")]

    texts = []
    for proj in proj_lst:
        tail = os.path.basename(os.path.normpath(proj))
        name = tail[:-8].lower()
        fil = f"{proj}/results.csv"
        if os.stat(fil).st_size != 0:
            with open(fil) as f:
                res = csv.reader(f, delimiter=" ")
                for row in res:
                    texts.append(row)

        cont = texts[1]
        txt = " ".join(cont)

        kw_extractor = yake.KeywordExtractor()
        text = txt
        language = "en"
        max_ngram_size = 1
        deduplication_threshold = 0.9
        numOfKeywords = 10
        custom_kw_extractor = yake.KeywordExtractor(
            lan=language,
            n=max_ngram_size,
            dedupLim=deduplication_threshold,
            top=numOfKeywords,
            features=None,
        )
        keywords = custom_kw_extractor.extract_keywords(text)
        punct_kwds = [
            i[0].translate(str.maketrans("", "", string.punctuation)) for i in keywords
        ]
        lower_kwds = [i.lower() for i in punct_kwds]
        dirty_kwds = [i.strip() for i in lower_kwds]

        badwords = [
            f"{name}",
            "package",
            "Python",
            "python",
            "PYTHON",
            "create",
            "collection",
            "Collection",
            "collections",
            "Collections",
            "used",
            "utility",
            "Utility",
            "utilities",
            "Utilities",
            "functions",
            "Functions",
            "function",
            "Function",
            "code",
            "Code",
            "again",
            "Again",
            "output",
            "codespace",
            "codespaces",
            "module",
            "modules",
            "install",
            "installing",
            "line",
            "lines",
            "nin",
            "library",
            "git",
            "svn",
            "command",
            "commands",
            "sends",
            "release",
            "releases",
            "documentation",
            "part",
            "elegant",
            "powerful",
            "current",
            "awesome",
            "implementation",
            "repository",
            "repositories",
            "username",
        ]

        kwds = []
        kwds_plural = [i for i in dirty_kwds if i not in badwords]

        for t in kwds_plural:
            slst = [o for o in kwds_plural if o != t]
            value = process.extractOne(t, slst)
            if value[1] < 90:
                kwds.append(t)

        similars = [u for u in kwds_plural if u not in kwds]
        if similars != []:
            sim_choice = max(similars, key=len)
            kwds += [sim_choice]

        with open(f"{proj}/kwds.txt", "w") as v:
            for k in kwds:
                v.write(f"{k}\n")


if __name__ == "__main__":
    kwd_creator()
