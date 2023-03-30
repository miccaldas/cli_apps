import os
import re
import subprocess

import snoop
import yake
from snoop import pp


def show_create_files():
    """"""
    cwd = os.getcwd()
    filefolder = f"{cwd}/pip_show_files"

    with open(f"{cwd}/requirements.txt", "r") as f:
        npacklst = f.readlines()
    packlst = [i.strip() for i in npacklst]

    for p in packlst:
        cmd = f"python -m pip show --verbose {p} > {filefolder}/{p}.txt"
        subprocess.run(cmd, shell=True)


def kwd_creation():
    cwd = os.getcwd()
    filefolder = f"{cwd}/pip_show_files"

    file = f"{filefolder}/bleach1.txt"
    with open(file, "r") as v:
        content = v.read()

    kw_extractor = yake.KeywordExtractor()
    text = content
    language = "en"
    max_ngram_size = 1
    deduplication_threshold = 0.9
    numOfKeywords = 3
    custom_kw_extractor = yake.KeywordExtractor(
        lan=language,
        n=max_ngram_size,
        dedupLim=deduplication_threshold,
        top=numOfKeywords,
        features=None,
    )
    keywords = custom_kw_extractor.extract_keywords(text)
    kwds = []


def urls():
    cwd = os.getcwd()
    filefolder = f"{cwd}/pip_show_files"

    lstfiles = os.listdir(filefolder)
    for f in lstfiles:
        cmd = f"sed -ne '/https:\/\/.*$/p' {filefolder}/{f} > urls/{f}"
        subprocess.run(cmd, shell=True)


@snoop
def readurls():
    cwd = os.getcwd()
    filefolder = f"{cwd}/pip_show_files"
    lnks = f"{cwd}/urls"

    fil = f"{lnks}/blinker.txt"

    urlline = []
    with open(fil, "r") as g:
        lins = g.readlines()
        for line in lins:
            urlline.append(line.strip())

    pp(urlline)


if __name__ == "__main__":
    readurls()
