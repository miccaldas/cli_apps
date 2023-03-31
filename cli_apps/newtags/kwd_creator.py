"""
Module Docstring
"""
import csv
import os
import string

import snoop
import yake
from snoop import pp

# import subprocess


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def kwd_creator():
    """"""

    cwd = os.getcwd()
    proj_folder = f"{cwd}/projects"

    # proj_lst = os.listdir(proj_folder)
    proj_lst = [
        f"{proj_folder}/yake_project",
        f"{proj_folder}/venusian_project",
        f"{proj_folder}/trio_project",
        f"{proj_folder}/schedule_project",
        f"{proj_folder}/rich_project",
    ]

    for proj in proj_lst:
        name = proj[:-8].lower()
        file = f"{proj_folder}/{proj}/results.csv"
        texts = []
        with open(file) as f:
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
        punct_kwds = [i[0].translate(str.maketrans("", "", string.punctuation)) for i in keywords]
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
        ]

        kwds = [i for i in dirty_kwds if i not in badwords]

        with open(f"{proj_folder}/{proj}/yake_kwds.txt", "w") as v:
            v.write(kwds)


if __name__ == "__main__":
    kwd_creator()
