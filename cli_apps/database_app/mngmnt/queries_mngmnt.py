"""
Houses all modules regarding fulltext searches.
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
def queries_expression():
    """
    Builds the SQL query string.
    First it creates a search for
    each query, then associates to
    them a 'union' string, which is
    a MySQL operation to join results
    of different expressions. We turn
    it back to a list of strings, delete
    the superflous final 'union' statement,
    add a order definition that should only
    came at the end of the query, and finally
    we turn it into a string. REady to be
    fed to the database.
    """
    with open("queries.bin", "rb") as f:
        queries = pickle.load(f)

    megaqry = []
    for i in queries:
        qry = f"SELECT * FROM cli_apps WHERE MATCH(name, presentation) AGAINST ('{i}')"
        megaqry.append((qry, " UNION "))
    megalst = [i for tup in megaqry for i in tup]
    megalst.pop(-1)
    megalst.append(" ORDER BY TIME")
    megastr = " ".join(megalst)

    with open("megastr.bin", "wb") as f:
        pickle.dump(megastr, f)


if __name__ == "__main__":
    queries_expression()


# @snoop
def get_queries():
    """
    Uses the expression created by 'queries_expression' to make
    a database call. Keeps results in a pickle file.
    """
    with open("megastr.bin", "rb") as f:
        query = pickle.load(f)

    qr = dbdata(query, "fetch")

    with open("qlst.bin", "wb") as g:
        pickle.dump(qr, g)


if __name__ == "__main__":
    get_queries()


# @snoop
def queries_mngmnt(queries):
    """
    Calls all query searches functions.
    """
    with open("queries.bin", "wb") as f:
        pickle.dump(queries, f)

    queries_expression()
    get_queries()

    os.remove("megastr.bin")
    os.remove("queries.bin")


if __name__ == "__main__":
    queries_mngmnt()
