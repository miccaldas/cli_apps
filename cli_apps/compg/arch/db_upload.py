"""
Where we prepare the data to be inserted on the db
and upload the clean version.
"""
import os
import pickle

import snoop
from cli_apps.database_app.db import dbdata
from cli_apps.database_app.methods import input_decision, print_template
from snoop import pp


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def data_preparation():
    """
    We gather information for the db columns from 'entries.bin'.
    """
    with open("epoch.bin", "rb") as f:
        epoch = pickle.load(f)
    with open("db_cull.bin", "rb") as g:
        entries = pickle.load(g)

    kwlst = os.listdir("kws")

    fin = []
    for k in kwlst:
        # We open this list inside the loop because, this way it'll be possible
        # to collect information about each loop turn. At the end of the turn we
        # collect the information to another list, and, come the next loop, the
        # first list is empty again, ready to restart.
        with open(f"kws/{k}", "r") as f:
            ks = f.readlines()
        # If keyBERT created 3 or more keyword, we gather the first three.
        if len(ks) >= 3:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = ks[2].strip()
            # We append the app name to the list of keywords, because one the tags
            # should always be its name.
            kl = [k, t2, t3, t4]
            # In the list that has the db's collected information, 'cleandata', we add
            # the keyowrd tuple to the dictionary with the a 'name' key equal to the first
            # element of kl. This value is a app name. Remember that 'update' in dictionaries,
            # is an expression that always outputs 'None'. plk's value will be 'None', but the
            # alteration to 'cleandata' will be done.
            for r in entries:
                print(r)
                if kl[0] == r[-1]:
                    print(kl)
                    ttgs = r + kl
                    # Don't forget to add data to the new db column, 'source'.
                    ttgs.append("compg")
                    fin.append(ttgs)
        if len(ks) == 2:
            t2 = ks[0].strip()
            t3 = ks[1].strip()
            t4 = "NA"
            kl = (k, t2, t3, t4)
            for r in entries:
                if kl[0] == r[-1]:
                    ttgs = r + [kl]
                    ttgs.append("compg")
                    fin.append(ttgs)
        if len(ks) == 1:
            t2 = ks[0].strip()
            t3 = "NA"
            t4 = "NA"
            kl = (k, t2, t3, t4)
            for r in entries:
                if kl[0] == r[-1]:
                    ttgs = r + kl
                    ttgs.append("compg")
                    fin.append(ttgs)

    # Another sanity check to see if the information is, really, ready to be uploaded.
    print_template(fin)
    print("\n")
    dec = input_decision("Do you want to continue?[y/n] ")
    if dec == "n":
        raise SystemExit

    with open(f"final_data_{epoch[0]}_{epoch[1]}.bin", "wb") as i:
        pickle.dump(fin, i)


if __name__ == "__main__":
    data_preparation()


@snoop
def db_upload():
    """
    We upload the data
    to the db.
    """
    with open("epoch.bin", "rb") as i:
        epoch = pickle.load(i)

    with open(f"final_data_{epoch[0]}_{epoch[1]}.bin", "rb") as f:
        d = pickle.load(f)

    for dt in d:
        name = dt[0]
        content = dt[1]
        url = dt[2]
        t0 = dt[3]
        t1 = dt[4]
        t2 = dt[5]
        t3 = dt[6]
        source = dt[7]
        q1 = "INSERT INTO cli_apps (name, presentation, url, t1, t2, t3, t4, source) VALUES "
        q2 = f"('{name}', '{content}', '{url}', '{t0}', '{t1}', '{t2}', '{t3}', '{source}')"
        query = f"{q1}{q2}"
        dbdata(query, "commit")


# if __name__ == "__main__":
#     db_upload()
