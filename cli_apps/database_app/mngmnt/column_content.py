"""
Collects column data for names or keywords,
if the user answered 'yes' in the initial
queries.
"""
import pickle

# import snoop
# from snoop import pp

from db import dbdata


# def type_watch(source, value):
#     return f"type({source})", type(value)


# snoop.install(watch_extras=[type_watch])


# @snoop
def column_content(query, out_binary):
    """
    We'll make a db call for the asked
    column and return it.
    """
    qrysrch = dbdata(query, "fetch")
    qs = [i[0] for i in qrysrch]

    with open(f"{out_binary}", "wb") as f:
        pickle.dump(qs, f)


if __name__ == "__main__":
    column_content()
