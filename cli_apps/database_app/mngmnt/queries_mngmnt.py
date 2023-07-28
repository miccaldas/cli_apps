"""
Houses all modules regarding fulltext searches.
"""
import os
import pickle

from mngmnt.get import get
from mngmnt.sql_expression import sql_expression

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def queries_mngmnt(queries):
    """
    Calls all query searches functions.
    """
    with open("queries.bin", "wb") as f:
        pickle.dump(queries, f)

    sql_expression("queries.bin", "megastr.bin")
    get("megastr.bin", "qlst.bin")

    os.remove("megastr.bin")
    os.remove("queries.bin")


if __name__ == "__main__":
    queries_mngmnt()
