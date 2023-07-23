"""
Houses all functions regarding id's.
"""
import snoop
from snoop import pp
import os
import pickle
from db import dbdata


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
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


@snoop
def get_ids():
    """
    With the SQL query built by 'ids_expression',
    we'll make a db call for the information
    regarding these ids.
    """
    with open("iqry.bin", "rb") as f:
        query = pickle.load(f)

    idinfo = dbdata(query, "fetch")

    with open("idinfo.bin", "wb") as g:
        pickle.dump(idinfo, g)


@snoop
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
