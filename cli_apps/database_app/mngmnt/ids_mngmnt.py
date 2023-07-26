"""
Houses all functions regarding id's.
"""
import os
import pickle

# import snoop
# from snoop import pp

from cli_apps.database_app.db import dbdata


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def ids_expression():
    """
    Builds the SQL statement to search the
    database by id numbers.
    """
    with open("ids.bin", "rb") as f:
        ids = pickle.load(f)

    idqry = []
    for i in ids:
        qr = f"SELECT * FROM cli_apps WHERE id = {i}"
        qry = qr.strip()
        idqry.append(qry)
        idqry.append(" UNION ")
    idqry.pop(-1)
    idqry.append(" ORDER BY TIME")
    iqry = " ".join(idqry)
    with open("iqry.bin", "wb") as f:
        pickle.dump(iqry, f)


if __name__ == "__main__":
    ids_expression()


# @snoop
def get_ids():
    """
    With the SQL query built by 'ids_expression',
    we'll make a db call for the information
    regarding these ids.
    """
    with open("iqry.bin", "rb") as f:
        query = pickle.load(f)

    idinfo = dbdata(query, "fetch")

    with open("ilst.bin", "wb") as g:
        pickle.dump(idinfo, g)


if __name__ == "__main__":
    get_ids()


# @snoop
def ids_mngmnt(ids):
    """
    Starts all id related functions.
    """
    with open("ids.bin", "wb") as f:
        pickle.dump(ids, f)

    ids_expression()
    get_ids()

    os.remove("ids.bin")
    os.remove("iqry.bin")


if __name__ == "__main__":
    ids_mngmnt()
