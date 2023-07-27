"""
We'll read the files in 'results' and turn it into a list of tuples.
We'll collect three keyword results per package, add it to results
and send it to a MySQL database.
"""
import os
import pickle

import snoop
from mysql.connector import Error, connect

# def type_watch(source, value):
#     return "type({})".format(source), type(value)


# snoop.install(watch_extras=[type_watch])

cwd = os.getcwd()


# @snoop
def kwd_collector():
    """
    We collect the keywords.
    """
    tags = f"{cwd}/tags"
    fldr = f"{tags}/kws"
    fllst = os.listdir(fldr)

    kwdlst = []
    for file in fllst:
        with open(f"{fldr}/{file}", "r") as f:
            kws = f.readlines()
            if len(kws) >= 3:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = kws[2].strip()
                kwdlst.append((f"{file}", t2, t3, t4))
            if len(kws) == 2:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = "NA"
                kwdlst.append((f"{file}", t2, t3, t4))
            if len(kws) == 1:
                t2 = kws[0].strip()
                t3 = "NA"
                t4 = "NA"
                kwdlst.append((f"{file}", t2, t3, t4))
            if kws == []:
                t2 = "NA"
                t3 = "NA"
                t4 = "NA"
                kwdlst.append((f"{file}", t2, t3, t4))

    with open(f"{tags}/kwdlst.bin", "wb") as f:
        pickle.dump(kwdlst, f)


if __name__ == "__main__":
    kwd_collector()


@snoop
def db_upload():
    """
    The database was previously created.
    So its just the case of iterating
    through the tuples, assign to each a
    to a column and the upload is
    complete.
    """
    folders = f"{cwd}/results/"
    tags = f"{cwd}/tags"
    paths = [os.path.join(folders, file) for file in os.listdir(folders)]
    with open(f"{tags}/kwdlst.bin", "rb") as f:
        kwdlst = pickle.load(f)

    for file in paths:
        with open(file, "r") as f:
            fdata = f.readlines()
            name = fdata[0].strip()
            kwds = [(a, b, c, d) for a, b, c, d in kwdlst if a == name]
            presentation = fdata[1].strip()
            url = fdata[2].strip()
            answers = [name, presentation, url]
            for k in kwds:
                answers += [k[0].lower()]
                answers += [k[1].lower()]
                answers += [k[2].lower()]
                answers += [k[3].lower()]
            answers += ["pip"]
            try:
                conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
                cur = conn.cursor()
                query = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4, source) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cur.execute(query, answers)
                conn.commit()
            except Error as e:
                print("Error while connecting to db", e)
            finally:
                if conn:
                    conn.close()


if __name__ == "__main__":
    db_upload()
