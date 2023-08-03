"""
Where we prepare the data to be inserted on the db
and upload the clean version.
"""
import os
import pickle

import snoop
from cli_apps.database_app.db import dbdata
from dotenv import load_dotenv
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])

load_dotenv()

# Envs
die = os.getenv("DIE")


# @snoop
def data_preparation():
    """
    We gather information for the db columns that
    is dispersed through various files, in one list.
    """
    with open(f"{die}clean_list.bin", "rb") as f:
        clean = pickle.load(f)
    with open(f"{die}spiders.bin", "rb") as g:
        spiders = pickle.load(g)

    # The first string from the spider's output is composed of the app's name
    # a dash and a small description. We'll use these values to insert into
    # the 'name' and 'description' columns. To do that we split the string at
    # the dash, the first part of the splitted string is the name, the other
    # the description.
    cleandata = [(i[0].split(" - ")[0], i[0].split(" - ")[1]) for i in clean]
    # We add the url value that was in the 'spiders.bin' file We define 'f' as
    # the current name/description tuples of 'cleandata' and to that we add the
    # link value in 'spiders', as tuple, for this is the way to insert an element
    # to a pre-existing tuple.
    plnk = [f + (t[2],) for f in cleandata for t in spiders if f[0] == t[0]]

    kwlst = os.listdir(f"{die}kws")

    data = []
    for k in kwlst:
        # We open this list inside the loop because, this way it'll be possible
        # to collect information about each loop turn. At the end of the turn we
        # collect the information to another list, and, come the next loop, the
        # first list is empty again, ready to restart.
        kl = []
        # We open the list of files with keywords. We'll open each one and iterate
        # through their content.
        with open(f"{die}kws/{k}", "r") as f:
            ks = f.readlines()
        # If keyBERT created 3 or more keyword, we gather the first three.
        if len(ks) >= 3:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = ks[2].strip()
            # We append the app name to the list of keywords, because one the tags
            # should always be its name.
            kl.append((k, t2, t3, t4))
            # In the list that has the db's collected information, 'plnk', we add
            # the keyowrd tuple to the tuple sharing the same name.
            ent = [h + kl[0] for h in plnk if h[0] == kl[0][0]]
            # So as not to have unnecessary levels, we do away with the tuple and keep
            # a list of lists structure.
            entry = [i for sub in ent for i in sub]
            # Don't forget to add data to the new db column, 'source'.
            entry += ["compg"]
            data.append(entry)
        if len(ks) == 2:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = "NA"
            kl.append((k, t2, t3, t4))
            ent = [h + kl[0] for h in plnk if h[0] == kl[0][0]]
            entry = [i for sub in ent for i in sub]
            entry += ["compg"]
            data.append(entry)
        if len(ks) == 1:
            t2 = ks[0].strip()
            t3 = "NA"
            t4 = "NA"
            kl.append((k, t2, t3, t4))
            ent = [h + kl[0] for h in plnk if h[0] == kl[0][0]]
            entry = [i for sub in ent for i in sub]
            entry += ["compg"]
            data.append(entry)

    with open(f"{die}final_data.bin", "wb") as g:
        pickle.dump(data, g)


if __name__ == "__main__":
    data_preparation()


@snoop
def db_upload():
    """
    We upload the data
    to the db.
    """
    with open(f"{die}final_data.bin", "rb") as f:
        dt = pickle.load(f)

    for d in dt:
        # For no reason but pretiness sake, I broke que query in two parts.
        q1 = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4, source) VALUES "
        q2 = f"('{d[0]}', '{d[1]}', '{d[2]}', '{d[3]}', '{d[4]}', '{d[5]}', '{d[6]}', '{d[7]}')"
        query = f"{q1}{q2}"
        dbdata(query, "commit")


if __name__ == "__main__":
    db_upload()
