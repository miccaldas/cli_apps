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
    query = "SELECT * FROM cli_apps WHERE t1 = %s OR t2 = %s OR t3 = %s OR t4 = %s  ORDER BY time"

    answers = ["cli", "mysql"]

    qr = dbdata(query, answers)
    print(qr)


if __name__ == "__main__":
    test()
