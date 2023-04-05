"""
Prepare and send keyword data to the *cli_apps* database.
"""
import os

import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def kwd_uploader():
    """
    We collect the keywords and upload them to the database.
    """
    fldr = f"{os.getcwd()}/kws"
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

    try:
        for tup in kwdlst:
            answers = [tup[1], tup[2], tup[3], tup[0]]
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "UPDATE cli_apps SET t2 = %s, t3 = %s, t4 = %s WHERE name = %s"
            cur.execute(query, answers)
            conn.commit()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    kwd_uploader()
