"""
From arguments and options of the cli request,
we're going to create sql expressions to query
the database.
"""
import pickle

import snoop
from snoop import pp

from db import dbdata


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def sql_expression(in_binary, out_binary):
    """
    We'll see what content there are
    in the output of the arguments/options,
    and turn them to a sql expression. that
    we'll pickle.
    """
    with open(f"{in_binary}", "rb") as f:
        asks = pickle.load(f)

    collection = []
    if in_binary == "queries.bin":
        qry = (
            "SELECT * FROM cli_apps WHERE MATCH(name, presentation) AGAINST ('dummy') "
        )
    if in_binary == "keywords.bin":
        qry = 'SELECT * FROM cli_apps WHERE t1 = "dummy" OR t2 = "dummy" OR t3 = "dummy" OR t4 = "dummy"'
    if in_binary == "ids.bin":
        qry = "SELECT * FROM cli_apps WHERE id = dummy"
    if in_binary == "names.bin":
        qry = "SELECT * FROM cli_apps WHERE name = 'dummy'"

    for ask in asks:
        # This is for keywords, to create an expression by keyword.
        if "t1" in qry:
            kqry = qry.replace("dummy", ask)
            collection.append(kqry)
        # Same for names.
        if "name = 'dummy'" in qry:
            nqry = qry.replace("dummy", ask)
            collection.append(nqry)
        # Id's
        if "id = 'dummy'" in qry:
            iqry = qry.replace("dummy", ask)
            collection.append(iqry)
        # Queries.
        if "('dummy')" in qry:
            qqry = qry.replace("dummy", ask)
            collection.append(qqry)

        collection.append(" UNION")
    collection.pop(-1)
    collection.append(" ORDER BY time")
    collection_str = " ".join(collection)

    insertdb = collection_str

    with open(f"{out_binary}", "wb") as g:
        pickle.dump(insertdb, g)


if __name__ == "__main__":
    sql_expression()
