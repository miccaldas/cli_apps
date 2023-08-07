"""
Houses all modules regarding fulltext searches.
"""
import os
import pickle
from dotenv import load_dotenv

from mngmnt.get import get
from mngmnt.sql_expression import sql_expression

# import snoop
# from snoop import pp


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])
load_dotenv()


# @snoop
def queries_mngmnt(queries):
    """
    Calls all query searches functions.
    """
    da = os.getenv("DA")

    with open(f"{da}queries.bin", "wb") as f:
        pickle.dump(queries, f)

    sql_expression(f"{da}queries.bin", f"{da}megastr.bin")
    get(f"{da}megastr.bin", f"{da}qlst.bin")

    os.remove(f"{da}megastr.bin")
    os.remove(f"{da}queries.bin")


if __name__ == "__main__":
    queries_mngmnt()
