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
mix = os.getenv("MIX")
project = os.getenv("MIXPROJ")
comp = os.getenv("COMP")


@snoop
def data_preparation():
    """
    We gather information for the db columns that
    is dispersed through various files, in one list.
    """
    with open(f"{mix}spiders.bin", "rb") as g:
        spiders = pickle.load(g)
    with open(f"{mix}clean_list.bin", "rb") as h:
        cleandata = pickle.load(h)
    with open(f"{comp}epoch.bin", "rb") as i:
        epoch = pickle.load(i)

    # There are times where the program chooses links that are very similar. For example, it sent us
    # these two url's:
    # 'https://manpages.debian.org/stretch/python3-numpy/f2py3.1'
    # 'https://manpages.debian.org/unstable/python3-numpy/f2py3.1'
    # If you're attentive you'll notice that they differ in the distribution, one's 'stretch' the other
    # is 'unstable'. Off course that doesn't suit us. To avoid this situation we'll be accepting only
    # the first link of a given app. Arbitrary I know, but it's less bad than leaving it as it is.
    names = []
    clean = []
    for c in cleandata:
        name = c[0]
        if name not in names:
            names.append(name)
            clean.append(c)
    cleandata = clean

    kwlst = os.listdir(f"{mix}kws")

    fin = []
    for k in kwlst:
        # We open this list inside the loop because, this way it'll be possible
        # to collect information about each loop turn. At the end of the turn we
        # collect the information to another list, and, come the next loop, the
        # first list is empty again, ready to restart.
        # We open the list of files with keywords. We'll open each one and iterate
        # through their content.
        with open(f"{mix}kws/{k}", "r") as f:
            ks = f.readlines()
        # If keyBERT created 3 or more keyword, we gather the first three.
        if len(ks) >= 3:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = ks[2].strip()
            # We append the app name to the list of keywords, because one the tags
            # should always be its name.
            kl = (k, t2, t3, t4)
            # In the list that has the db's collected information, 'cleandata', we add
            # the keyowrd tuple to the dictionary with the a 'name' key equal to the first
            # element of kl. This value is a app name. Remember that 'update' in dictionaries,
            # is an expression that always outputs 'None'. plk's value will be 'None', but the
            # alteration to 'cleandata' will be done.
            for r in cleandata:
                if kl[0] == r[0]:
                    ttgs = r + (kl[1], kl[2], kl[3])
                    # Don't forget to add data to the new db column, 'source'.
                    tall = ttgs + ("compg",)
                    fin.append(tall)
        if len(ks) == 2:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = "NA"
            kl = (k, t2, t3, t4)
            for r in cleandata:
                ttgs = r + (kl[1], kl[2], kl[3])
                tall = ttgs + ("compg",)
                fin.append(tall)
        if len(ks) == 1:
            t2 = ks[0].strip()
            t3 = "NA"
            t4 = "NA"
            kl = (k, t2, t3, t4)
            for r in cleandata:
                ttgs = r + (kl[1], kl[2], kl[3])
                tall = ttgs + ("compg",)
                fin.append(tall)

    print(fin)
    with open(f"{mix}final_data_{epoch[0]}_{epoch[1]}.bin", "wb") as i:
        pickle.dump(fin, i)


if __name__ == "__main__":
    data_preparation()


@snoop
def db_upload():
    """
    We upload the data
    to the db.
    """
    with open(f"{comp}epoch.bin", "rb") as i:
        epoch = pickle.load(i)
    low = epoch[0]
    high = epoch[1]

    with open(f"{mix}final_data_{epoch[0]}_{epoch[1]}.bin", "rb") as f:
        d = pickle.load(f)

    dt = d[0]
    name = dt[0]
    content = dt[2]
    print(content)
    url = dt[1]
    print(url)
    t0 = dt[0]
    t1 = dt[3]
    t2 = dt[3]
    print(t2)
    t3 = dt[4]
    print(t3)
    t4 = dt[5]
    print(t4)

    q1 = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4, source) VALUES "
    q2 = f"('{name}', '{content}', '{url}', '{name}', '{t1}', '{t2}', '{t3}', '{t4}')"
    query = f"{q1}{q2}"
    dbdata(query, "commit")


# if __name__ == "__main__":
#     db_upload()
