"""
Analyzes the content of 'results.csv' in each Scrapy project folder.
Generates keywords per project. Writes a 'kwds_2.txt' file next to
'results.csv'.
This file was ran from inside the 'projects' folder.
"""
import csv
import os
import string
import sys

import snoop
from keybert import KeyBERT
from snoop import pp
from thefuzz import fuzz, process


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


# @snoop
def kwd_creator():
    """
    Iterates through the csv files with Scrapy's scraped
    information, reads them, cleans the text, searches for
    keywords and writes what if finds in txt file.
    """

    # Get the location of 'projects' folder.
    cwd = os.getcwd()

    # Python was throwing an error that the 'csv' field was too small.
    # This extends it to the meximum.
    csv.field_size_limit(sys.maxsize)
    # List with the names of the projects.
    projlst = os.listdir(cwd)
    # List of folders only.
    proj_lst = [w for w in projlst if w.endswith("_project")]

    for proj in proj_lst:
        texts = []
        # Define only the last part of a path.
        tail = os.path.basename(os.path.normpath(proj))
        # Get the package name only and in lowercase.
        name = tail[:-8].lower()
        # Path to the results file inside the folders.
        fil = f"{proj}/results.csv"
        # Checks if file is empty or not.
        if os.stat(fil).st_size != 0:
            with open(fil) as f:
                # Reads each line in 'csv' file and adds it to a list.
                res = csv.reader(f, delimiter=" ")
                for row in res:
                    texts.append(row)
            # First line is the column name and we don't need it.
            cntnt = texts[1]
            # KeyBERT only works with strings, so we turn the list to string.
            text = " ".join(cntnt)

            badwords = [
                f"{name}",
                f"n{name}",
                "package",
                "Python",
                "python",
                "npython",
                "py",
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
                "codes",
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
                "parse",
                "work",
                "open",
                "solution",
                "case",
                "studies",
                "explore",
                "level",
                "program",
                "programs",
                "programming",
                "Program",
                "Programs",
                "computing",
                "github",
                "application",
                "applications",
                "toolkit",
                "pip",
                "Pip",
                "install",
                "Install",
                "installs",
                "installed",
                "scripting",
                "scripts",
                "script",
                "whitespace",
                "file",
                "files",
                "codebase",
                "directory",
                "cli",
                "import",
                "imports",
                "importing",
            ]

            # Declaring KeyBERT.
            kw_model = KeyBERT()
            # Here we define that we're looking for keywords, not keyphrases,
            # with length of one word, excluding the words defined in "badwords".
            keyws = kw_model.extract_keywords(
                text,
                keyphrase_ngram_range=(1, 1),
                stop_words=badwords,
            )
            # Each result is presented as a tuple of keyword and its value. Here
            # we choose only the keyword.
            keywords = [o for o, p in keyws]
            # # In the beginning I saw a lot of very similar words, repeating the
            # same ideas. This loops helps in weeding them out.
            kwds = []
            for t in keywords:
                # As we are comparing keywords with other keywords of the same list,
                # we need to ensure that they are never compared to themselves.
                slst = [k for k in keywords if k != t]
                # In the beginning we were looking for very keyowrds, and this list
                # sometimes would be empty. This check is to avoid an error.
                if slst != []:
                    value = process.extractOne(t, slst)
                    # If a keyword is reasonably different from the others, it goes to
                    # the 'kwds' list.
                    if value[1] < 85:
                        kwds.append(t)
            # All the words that weren't different enough, go here.
            similars = [u for u in keywords if u not in kwds]
            # If any, from them we choose, arbitrarily, the longest one. This is to preffer
            # plural forms to singular ones.
            if similars != []:
                sim_choice = max(similars, key=len)
                # Add longest keyword, back with the other ones.
                kwds += [sim_choice]
            # Write results to file.
            with open(f"{proj}/kwds_2.txt", "w") as v:
                for k in kwds:
                    v.write(f"{k}\n")


if __name__ == "__main__":
    kwd_creator()
