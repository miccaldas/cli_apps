"""
Add thre keywords to the *newnames* entries and upload it to the db.
"""
import os
import pickle

# import snoop
# from snoop import pp

from db import dbdata


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])

yay = "/home/mic/python/cli_apps/cli_apps/yay_data/"


# @snoop
def kwd_collector():
    """
    We collect the *Arch* keywords and joint them with the rest of the data.
    """
    fldr = f"{yay}kws"
    fllst = os.listdir(fldr)

    with open("newnames.bin", "rb") as v:
        nn = pickle.load(v)

    kwdlst = []
    for file in fllst:
        with open(f"{fldr}/{file}", "r") as f:
            kws = f.readlines()
            if len(kws) >= 3:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = kws[2].strip()
                # Adding the keywords to the description', 'url' data.
                # We first select 'description' and 'url' from the list
                # of packages, where the 'name' in the list is the same
                # as the name in the file being read.
                ndata = [(c[0], c[1], c[2], c[0], t2, t3, t4) for c in nn if c[0] == f"{file}"]
                kwdlst.append(ndata)
            if len(kws) == 2:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = "NA"
                ndata = [(c[0], c[1], c[2], c[0], t2, t3, t4) for c in nn if c[0] == f"{file}"]
                kwdlst.append(ndata)
            if len(kws) == 1:
                t2 = kws[0].strip()
                t3 = "NA"
                t4 = "NA"
                ndata = [(c[0], c[1], c[2], c[0], t2, t3, t4) for c in nn if c[0] == f"{file}"]
                kwdlst.append(ndata)
            if kws == []:
                t2 = "NA"
                t3 = "NA"
                t4 = "NA"
                ndata = [(c[0], c[1], c[2], c[0], t2, t3, t4) for c in nn if c[0] == f"{file}"]
                kwdlst.append(ndata)
    with open(f"{yay}kwdlst.bin", "wb") as f:
        pickle.dump(kwdlst, f)


if __name__ == "__main__":
    kwd_collector()


# @snoop
def db_upload():
    """
    We'll iterate through the *kws* files, add them to the *Arch* data,
    clean the results for *MySQL*, and upload the new entries to *cli_apps*.\n
    .. code-block:: sql

        INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4) VALUES (%s, %s, %s, %s, %s, %s, %s)

    Then we'll upload the entries that were already in the db but lacked tag values.\n
    .. code-block:: sql

        UPDATE cli_apps SET t2 = %s, t3 = %s, t4 = %s WHERE name = %s
    """

    with open(f"{yay}kwdlst.bin", "rb") as f:
        kwdlst = pickle.load(f)

    kl = [i for sub in kwdlst for i in sub]
    for new in kl:
        answers = [new[0], new[1], new[2], new[3], new[4], new[5], new[6]]
        query = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        dbdata(query, "commit", answers)


if __name__ == "__main__":
    db_upload()
