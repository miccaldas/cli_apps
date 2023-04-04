"""
This module creates and inserts the new entries in the db.
"""
import os
import pickle

import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def dc():
    """
    Create a list of Scrapy projects that aren't in the db.
    """
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT name FROM cli_apps"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    recs = [i for g in records for i in g]

    with open("requirements.txt", "r") as f:
        allpip = f.readlines()

    all_pip = [v.strip() for v in allpip]
    left = [i for i in all_pip if i not in recs]

    with open("left.bin", "wb") as g:
        pickle.dump(left, g)


@snoop
def get_pip_show_info():
    """
    Create lists of the pip files and pip files of projects not in db.
    """
    with open("left.bin", "rb") as f:
        left = pickle.load(f)
    sleft = [o.lower() for o in left]

    cwd = os.getcwd()
    pipfiles = f"{cwd}/pip_show_files"
    piplst = os.listdir(f"{pipfiles}")
    with open("piplst.bin", "wb") as d:
        pickle.dump(piplst, d)

    leftpip = [i for i in piplst if i[:-4] in sleft]
    with open("leftpip.bin", "wb") as r:
        pickle.dump(leftpip, r)


@snoop
def get_pip_info():
    """
    Collect information from the files that resulted from
    the 'pip show command', that aren't in the db.
    """

    with open("leftpip.bin", "rb") as f:
        leftpip = pickle.load(f)

    for file in leftpip:
        with open(f"pip_show_files/{file}", "r") as u:
            content = u.readlines()
        pipinfo = []
        for line in content:
            if line.startswith("Name: "):
                if len(line) > 7:
                    pipinfo.append(line[5:].strip())
            if line.startswith("Summary: "):
                if len(line) > 11:
                    pipinfo.append(line[9:].strip())
            if line.startswith("Home-page: "):
                if len(line) > 12:
                    pipinfo.append(line[11:].strip())
            if len(pipinfo) != 3:
                if line.startswith("  Homepage, "):
                    if len(line) > 15:
                        pipinfo.append(line[13:].strip())

        try:
            conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
            cur = conn.cursor()
            query = "INSERT INTO cli_apps (name, presentation, url) VALUES (%s, %s, %s)"
            cur.execute(query, pipinfo)
            conn.commit()
        except Error as e:
            print("Error while connecting to db", e)
        finally:
            if conn:
                conn.close()


@snoop
def get_kwd_info():
    """
    Upload the keyword data of the lacking projects.
    """
    with open("kwlst.bin", "rb") as f:
        kwlst = pickle.load(f)

    with open("leftpip.bin", "rb") as f:
        leftpip = pickle.load(f)

    kwdleft = [i for i in kwlst if i[0][61:] + ".txt" in leftpip]

    try:
        for k in kwdleft:
            name = k[0][61:]
            if len(k[1]) >= 3:
                t2 = k[1][0]
                t3 = k[1][1]
                t4 = k[1][2]
            if len(k[1]) == 2:
                t2 = k[1][0]
                t3 = k[1][1]
                t4 = "NA"
            if len(k[1]) == 1:
                t2 = k[1][0]
                t3 = "NA"
                t4 = "NA"
            answers = [t2, t3, t4, name]
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


@snoop
def stragglers():
    """
    Due to confusions in file naming, from the pip form to
    file form etc; a lot of entries weren't uploaded. We
    try again.
    """
    try:
        conn = connect(host="localhost", user="mic", password="xxxx", database="cli_apps")
        cur = conn.cursor()
        query = "SELECT name FROM cli_apps WHERE t2 = 'NA'"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    recs = [f for g in records for f in g]
    rcs = [v.replace("-", "_") for v in recs]

    with open("kwlst.bin", "rb") as f:
        kwlst = pickle.load(f)

    kwdlft = [i for i in kwlst if i[0][61:] in rcs]
    kwdleft = [(p[61:].replace("_", "-"), a) for p, a in kwdlft]

    try:
        for k in kwdleft:
            name = k[0]
            if len(k[1]) >= 3:
                t2 = k[1][0]
                t3 = k[1][1]
                t4 = k[1][2]
            if len(k[1]) == 2:
                t2 = k[1][0]
                t3 = k[1][1]
                t4 = "NA"
            if len(k[1]) == 1:
                t2 = k[1][0]
                t3 = "NA"
                t4 = "NA"
            answers = [t2, t3, t4, name]
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


@snoop
def stragglers1():
    """
    At this moment I said: Fuck it, I'll do it by hand.
    """

    klst = [
        ("python_levenshtein", "levenshtein", "gnu", "computation"),
        ("flask-login", "flask", "login", "error"),
        ("flask_humanize", "flask", "jinja", "humanize"),
        ("backports_csv", "csv", "encoding", "backports"),
        ("zc_lockfile", "interprocess", "zc", "lockfile"),
    ]

    try:
        for k in klst:
            answers = [k[1], k[2], k[3], k[0]]
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
    stragglers1()
