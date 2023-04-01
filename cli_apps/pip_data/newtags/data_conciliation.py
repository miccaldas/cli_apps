"""
Cleans and conciliates the data drawn from Pip with data from the database.
"""
import os
import pickle
import re

import snoop
from mysql.connector import Error, connect
from snoop import pp


def type_watch(source, value):
    return "type({})".format(source), type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def data_collection():
    """
    We gather the information needed from 'projects' and the
    database and turn them to pickle files; to be analyzed on
    other functions.
    """
    cwd = f"{os.getcwd()}/projects"
    projlst = os.listdir(cwd)
    proj_lst = [f"{cwd}/{i}" for i in projlst if i.endswith("_project")]

    kwd_tups = []
    for proj in proj_lst:
        with open(f"{proj}/kwds_2.txt", "r") as f:
            ktp = f.readlines()
            ktup = [i.strip() for i in ktp]
            name = proj[:-8].lower()
            if ktup != []:
                kwd_tups.append((name, ktup))

    # The csv file of 'jieba' has no inteligible words. We avoid it.
    kwlst = [(a, b) for a, b in kwd_tups if a != "jieba"]

    with open("kwlst.bin", "wb") as d:
        pickle.dump(kwlst, d)

    try:
        conn = connect(
            host="localhost", user="mic", password="xxxx", database="cli_apps"
        )
        cur = conn.cursor()
        query = "SELECT name FROM cli_apps ORDER BY name ASC"
        cur.execute(query)
        records = cur.fetchall()
    except Error as e:
        print("Error while connecting to db", e)
    finally:
        if conn:
            conn.close()

    # Results come as one item tuples. We clean it up.
    fltrecs = [g for h in records for g in h]
    with open("fltrecs.bin", "wb") as v:
        pickle.dump(fltrecs, v)
    # List of Scrapy projects names, to compare with the db.
    kanms = [z for z, x in kwlst]
    knm = [os.path.basename(os.path.normpath(u)) for u in kanms]
    knms = [p.lower() for p in knm]
    with open("knames.bin", "wb") as f:
        pickle.dump(knms, f)


# if __name__ == "__main__":
#     data_collection()


@snoop
def data_comparison():
    """
    We compare the content of the db and the updated
    data from Pip, and create two lists, one of keywords
    from packages already in the database, and those who
    are not. Each will be treated differently.
    """
    # Gettiing the list of the keywords in the Scrapy projects.
    knames = []
    with open("knames.bin", "rb") as f:
        while True:
            try:
                knames.append(pickle.load(f))
            except EOFError:
                break
    # Because it's a list of lists, we flatten it.
    keysn = [i for sublst in knames for i in sublst]

    # As we had to change the packages names so as to conform with rules
    # for naming Linux folders, we now have to do the opposite. So we can
    # compare the names of the Scrapy projects to db's entries, when uploading
    # to it.
    # First we change back some packages who had a '.' in the name:
    kname = []
    for k in keysn:
        kname.append(k)
        if k.startswith("jaraco"):
            po = k.replace("_", "-")
            kname.append(po)
    k_no_underscore = [n for n in kname if not n.startswith("jaraco_")]
    # Then we change back to dashes, the packages we had replaced by underscores.
    packages = []
    for y in k_no_underscore:
        packages.append(y)
        if "_" in y:
            y = y.replace("_", "-")
            packages.append(y)
    packs = [g for g in packages if "_" not in g]

    # Getting the list of db's packages names.
    fltrecs = []
    with open("fltrecs.bin", "rb") as d:
        while True:
            try:
                fltrecs.append(pickle.load(d))
            except EOFError:
                break
    # Flatten it as it's a list of lists.
    fltrec = [g for h in fltrecs for g in h]

    # List of Scrapy projects not on db.
    pcks_not_db = [i for i in packs if i not in fltrec]
    with open("pcks_not_db.bin", "wb") as m:
        pickle.dump(pcks_not_db, m)
    # List of Scrapy projects in the db.
    pcks_in_db = [b for b in packs if b not in pcks_not_db]
    with open("pcks_in_db.bin", "wb") as q:
        pickle.dump(pcks_in_db, q)


# if __name__ == "__main__":
#     data_comparison()


@snoop
def in_db_upld():
    """
    We'll upload the keywords of the projects
    already in the database.
    """

    # Getting list of project names already in db.
    in_db = []
    with open("pcks_in_db.bin", "rb") as f:
        while True:
            try:
                in_db.append(pickle.load(f))
            except EOFError:
                break

    # List of all projects and their keyword data.
    proj_data = []
    with open("kwlst.bin", "rb") as g:
        while True:
            try:
                proj_data.append(pickle.load(g))
            except EOFError:
                break
    # Flattening it out.
    pro_data = [g for h in proj_data for g in h]
    # For some reason, the project names came as paths not strings, as it should've been.
    # We change it now.
    projdata = [(h[61:], i) for h, i in pro_data]

    # Uploading to db.
    try:
        for proj in projdata:
            # The project name corresponds to the 'name' column in db.
            name = proj[0]
            # If there's 3 or more keywords, they'll be assigned to the 3
            # tag columns that are empty.
            # These columns have a default value, so there'll be something
            # written, even if the keyword number is less than 3.
            if len(proj[1]) >= 3:
                t2 = proj[1][0]
                t3 = proj[1][1]
                t4 = proj[1][2]
            if len(proj[1]) == 2:
                t2 = proj[1][0]
                t3 = proj[1][1]
            if len(proj[1]) == 1:
                t2 = proj[1][0]
            answers = [t2, t3, t4, name]
            conn = connect(
                host="localhost", user="mic", password="xxxx", database="cli_apps"
            )
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
def out_db_info_collection():
    """"""

    with open("pcks_not_db.bin", "rb") as f:
        not_db = pickle.load(f)

    cwd = os.getcwd()
    pip_files = f"{cwd}/pip_show_files"
    file = f"{pip_files}/goose3.txt"

    with open(file, "r") as f:
        content = f.readlines()

    answers = []
    for line in content:
        if line.startswith("Name: "):
            answers.append(line[6:].strip())

    url = []
    for line in content:
        if line.startswith("Home-page"):
            if len(line) > 13:
                url.append(line[11:].strip())
        if re.match(".+\sHomepage", line):
            clean_line = line.strip()
            if len(clean_line) > 11:
                url.append(clean_line[11:].strip())

    pp(url)
    pp(answers)


if __name__ == "__main__":
    out_db_info_collection()
