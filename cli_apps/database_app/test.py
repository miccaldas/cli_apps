"""
Module Docstring
"""
import snoop
from snoop import pp

# import os
# import subprocess
from db import dbdata


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@snoop
def test():
    """"""
    query = "SELECT * FROM cli_apps WHERE id = 3273"

    qr = dbdata(query, "fetch")
    print(qr)


if __name__ == "__main__":
    test()
