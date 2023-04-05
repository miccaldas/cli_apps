"""
We extract name, description and url information from the *pip show* files,
and create new files with this data in the *results* folder.
"""
import os
import re
import subprocess

import snoop
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def extract_file_info():
    """
    We iterate through the files in *package_files*, search for the
    entries we want for the database, prune them, to get only the
    data, and create a new file in the *results* folder. These files
    will be ready to be uploaded.
    """
    cwd = os.getcwd()
    results = f"{cwd}/results/"
    texts = f"{cwd}/package_files/"
    pckg_files = os.listdir(texts)

    for file in pckg_files:
        data = []
        with open(f"{texts}{file}", "r") as f:
            content = f.readlines()
        for line in content:
            if line.startswith("Name: "):
                nmln = line[6:].strip()
                data.append(nmln)
            if line.startswith("Summary: "):
                if len(line) > 11:
                    smln = line[9:].strip()
                else:
                    smln = "NA"
                data.append(smln)
            if line.startswith("Home-page: "):
                if len(line) > 12:
                    hpln = line[11:].strip()
                else:
                    hpln = "NA"
                data.append(hpln)
        with open(f"{results}/{file}", "w") as v:
            for d in data:
                v.write(f"{d}\n")


if __name__ == "__main__":
    extract_file_info()
