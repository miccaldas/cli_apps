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
deb = os.getenv("DEB")
project = os.getenv("DEBPROJ")
comp = os.getenv("COMP")


@snoop
def data_preparation():
    """
    We gather information for the db columns that
    is dispersed through various files, in one list.
    """
    with open(f"{deb}spiders.bin", "rb") as g:
        spiders = pickle.load(g)
    with open(f"{deb}finalized.bin", "rb") as h:
        cleandata = pickle.load(h)
    with open(f"{comp}epoch.bin", "rb") as i:
        epoch = pickle.load(i)

    low = epoch[0]
    high = epoch[1]

    # There are times where the program chooses links that are very similar. For example, it sent us
    # these two url's:
    # 'https://manpages.debian.org/stretch/python3-numpy/f2py3.1'
    # 'https://manpages.debian.org/unstable/python3-numpy/f2py3.1'
    # If you're attentive you'll notice that they differ in the distribution, ome's 'stretch' the other
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

    # We add the url value in 'spiders.bin' to 'cleandata'. This method changes 'cleandata' directly,
    # 'plnk' is just there to give a name to the comprehension. It's of no use to us from this point
    # onwards. It's important to know that the output of'plnk' will be a list of 'None' values. That's
    # because the update() method returns always 'None'. But if you look at 'cleandata' now, you'll see
    # that the url value was indeed added.
    # This was necessary because cleandata is list of dictionaries and spiders is a list of lists.
    # update() alters a dictionary data, and can add 'key: value' element to it.
    # What this comprehension is saying is: while iterating through 'cleandata' and 'spiders', and 'i'
    # being an index value, find where 'cleandata[i][0]' is equal to 'spiders[i][0]'; if you do find it,
    # create a new element in 'cleandata' with the key 'url' and the 'spiders[i][2]' as vaiue.
    plnk = [c.update({"url": f"{s[2]}"}) for c in cleandata for s in spiders if c["name"] == s[0]]

    # 'content' comes with '<app_name> - ' prefix that we don't need. We take it out.
    for i, t in enumerate(cleandata):
        cleandata[i].update({"content": cleandata[i]["content"].split(" - ")[1]})

    # To facilitate the MySQL's data insertion, we turn the 'content' list to string.
    for i, t in enumerate(cleandata):
        cleandata[i].update({"content": " ".join(cleandata[i]["content"])})

    kwlst = os.listdir(f"{deb}kws")

    for k in kwlst:
        # We open this list inside the loop because, this way it'll be possible
        # to collect information about each loop turn. At the end of the turn we
        # collect the information to another list, and, come the next loop, the
        # first list is empty again, ready to restart.
        # We open the list of files with keywords. We'll open each one and iterate
        # through their content.
        with open(f"{deb}kws/{k}", "r") as f:
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
            plk = [r.update({"tags": kl}) for r in cleandata if r["name"] == kl[0]]
            # Don't forget to add data to the new db column, 'source'.
            pk = [r.update({"source": "compg"}) for r in cleandata]
        if len(ks) == 2:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = "NA"
            kl = (k, t2, t3, t4)
            plnk = [c.update({"tags": kl}) for c in cleandata if c["name"] == kl[0]]
            pk = [r.update({"source": "compg"}) for r in cleandata]
        if len(ks) == 1:
            t2 = ks[0].strip()
            t3 = "NA"
            t4 = "NA"
            kl = (k, t2, t3, t4)
            plnk = [c.update({"tags": kl}) for c in cleandata if c["name"] == kl[0]]
            pk = [r.update({"source": "compg"}) for r in cleandata]

    print(cleandata)
    with open(f"{deb}final_data_{low}_{high}.bin", "wb") as i:
        pickle.dump(cleandata, i)


if __name__ == "__main__":
    data_preparation()


@snoop
def db_upload():
    """
    We upload the data
    to the db.
    """
    with open(f"{deb}final_data.bin", "rb") as f:
        dt = pickle.load(f)

    name = f"{dt[0]['name']}"
    content = f'{dt[0]["content"]}'
    print(content)
    url = f"{dt[0]['url']}"
    print(url)
    t1 = f"{dt[0]['name']}"
    print(type(dt[0]["tags"]))
    t2 = f"{dt[0]['tags'][1]}"
    print(t2)
    t3 = f"{dt[0]['tags'][2]}"
    print(t3)
    t4 = f"{dt[0]['tags'][3]}"
    print(t4)

    q1 = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4, source) VALUES "
    q2 = f"('{name}', '{content}', '{url}', '{name}', '{t1}', '{t2}', '{t3}', '{t4}')"
    query = f"{q1}{q2}"
    dbdata(query, "commit")


if __name__ == "__main__":
    db_upload()
