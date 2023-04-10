"""
We'll read the files in *results* and turn it into a list of tuples.
We'll collect three keyword results per package, add it to *results*
and send it to a MySQL database.
"""
import os
import pickle
import subprocess

# import snoop
from mysql.connector import Error, connect

# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def kwd_collector():
    """
    We collect the *Arch* keywords and joint them with the rest of the data.
    """
    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    fldr = f"{tags}/kws"
    fllst = os.listdir(fldr)

    with open(f"{tags}/newname.bin", "rb") as v:
        newname = pickle.load(v)

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
                nndata = [(c.strip(), d.strip()) for a, b, c, d in newname if b.strip() == f"{file}"]
                kwdlst.append(
                    (
                        f"{file}",
                        f"{nndata[0][0]}",
                        f"{nndata[0][1]}",
                        f"{file}",
                        t2,
                        t3,
                        t4,
                    )
                )
            if len(kws) == 2:
                t2 = kws[0].strip()
                t3 = kws[1].strip()
                t4 = "NA"
                nndata = [(c.strip(), d.strip()) for a, b, c, d in newname if b.strip() == f"{file}"]
                kwdlst.append(
                    (
                        f"{file}",
                        f"{nndata[0][0]}",
                        f"{nndata[0][1]}",
                        f"{file}",
                        t2,
                        t3,
                        t4,
                    )
                )
            if len(kws) == 1:
                t2 = kws[0].strip()
                t3 = "NA"
                t4 = "NA"
                nndata = [(c.strip(), d.strip()) for a, b, c, d in newname if b.strip() == f"{file}"]
                kwdlst.append(
                    (
                        f"{file}",
                        f"{nndata[0][0]}",
                        f"{nndata[0][1]}",
                        f"{file}",
                        t2,
                        t3,
                        t4,
                    )
                )
            if kws == []:
                t2 = "NA"
                t3 = "NA"
                t4 = "NA"
                nndata = [(c.strip(), d.strip()) for a, b, c, d in newname if b.strip() == f"{file}"]
                kwdlst.append(
                    (
                        f"{file}",
                        f"{nndata[0][0]}",
                        f"{nndata[0][1]}",
                        f"{file}",
                        t2,
                        t3,
                        t4,
                    )
                )
    with open(f"{tags}/kwdlst.bin", "wb") as f:
        pickle.dump(kwdlst, f)


if __name__ == "__main__":
    kwd_collector()


# Suggested by Sourcery. Encapsulates repeated
# db execution code, as there are three calls
# to the db in 'db_upload' into one block of code.
def execute_db(cur, query, answers, conn):
    cur.execute(query, answers)
    conn.commit()
    conn.close()


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

    tags = "/home/mic/python/cli_apps/cli_apps/yay_data/tags"
    with open(f"{tags}/kwdlst.bin", "rb") as f:
        kwdlst = pickle.load(f)
    with open("/home/mic/python/cli_apps/cli_apps/yay_data/newnames.bin", "rb") as f:
        oldnames = pickle.load(f)

    # The 'kwdlst.bin' file has both the new entries and the ones that only lacked tags.
    # Because they will have to be uploaded with different queries, we remove the new
    # entries from 'kwdlst.bin' and put them in a new list.
    newnames = []
    for n in range(len(oldnames)):
        for k in range(len(kwdlst)):
            if oldnames[n][0].strip() == kwdlst[k][0].strip():
                newnames.append(kwdlst[k])
                kwdlst.pop(k)

    # Upload for the new entries.
    if newnames != []:
        try:
            for new in newnames:
                answers = [new[0], new[1], new[2], new[3], new[4], new[5], new[6]]
                conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
                cur = conn.cursor()
                query = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                execute_db(cur, query, answers, conn)
        except Error as e:
            print("Error while connecting to db", e)

    # Upload for the entries who only lacked tags.
    if kwdlst != []:
        try:
            query = "UPDATE cli_apps SET t2 = %s, t3 = %s, t4 = %s WHERE name = %s"
            for lst in kwdlst:
                answers = [lst[4], lst[5], lst[6], lst[0]]
                conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
                cur = conn.cursor()
                execute_db(cur, query, answers, conn)
        except Error as e:
            print("Error while connecting to db", e)


if __name__ == "__main__":
    db_upload()
