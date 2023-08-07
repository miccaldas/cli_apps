"""
Houses all functions regarding id's.
"""
import os
import pickle

from cli_apps.database_app.db import dbdata
from dotenv import load_dotenv

# import snoop
# from snoop import pp
from mngmnt.get import get
from mngmnt.sql_expression import sql_expression

# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])

load_dotenv()


# @snoop
def ids_mngmnt(ids):
    """
    Starts all id related functions.
    """
    da = os.getenv("da")

    with open(f"{da}ids.bin", "wb") as f:
        pickle.dump(ids, f)

    sql_expression(f"{da}ids.bin", f"{da}iqry.bin")
    get(f"{da}iqry.bin", f"{da}ilst.bin")


if __name__ == "__main__":
    ids_mngmnt()
