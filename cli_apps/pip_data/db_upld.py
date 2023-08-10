"""
We'll read the files in 'results' and turn it into a list of tuples.
We'll collect three keyword results per package, add it to results
and send it to a MySQL database.
"""
import os
import pickle

from db import dbdata

# import snoop


# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def db_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the tuples, assign to each
    element a column and the upload is
    complete.
    """
    pip = "/home/mic/python/cli_apps/cli_apps/pip_data"
    with open(f"{pip}/kwdlst.bin", "rb") as f:
        kwdlst = pickle.load(f)

    # 'kl' as sublists around a single tuple. This is unnecessary hierarchization.
    # We get rid of the sublists, building a list of tuples.
    kl = [i for sub in kwdlst for i in sub]
    for k in kl:
        answers = [k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7]]
        query = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4, source) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        dbdata(query, "commit", answers)


if __name__ == "__main__":
    db_upload()
