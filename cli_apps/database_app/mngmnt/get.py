"""
Makes database calls from the SQL expressions
produced by 'expressions'.
"""
import pickle

# import snoop
# from snoop import pp

from db import dbdata


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def get(in_binary, out_binary):
    """
    The db call, which expression is
    taken from a pickled file, is made
    here. We pickle its results.
    """
    with open(f"{in_binary}", "rb") as f:
        query = pickle.load(f)

    qr = dbdata(query, "fetch")

    with open(f"{out_binary}", "wb") as g:
        pickle.dump(qr, g)


if __name__ == "__main__":
    get()
