"""
Houses all functions regarding id's.
"""
import os
import pickle

from cli_apps.database_app.db import dbdata

# import snoop
# from snoop import pp
from mngmnt.get import get
from mngmnt.sql_expression import sql_expression

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def ids_mngmnt(ids):
    """
    Starts all id related functions.
    """
    with open("ids.bin", "wb") as f:
        pickle.dump(ids, f)

    sql_expression("ids.bin", "iqry.bin")
    get("iqry.bin", "ilst.bin")


if __name__ == "__main__":
    ids_mngmnt()
