"""
Search module that'll aggreagate several search modes, like natural search
and tag search, to broaden the scope of the information that' given.
"""
import os
import subprocess

import click
import snoop
from snoop import pp

from ids_mngmnt import ids_mngmnt
from kwd_mngmnt import kwd_mngmnt
from methods import aggregate_info, checkinfo, srch_allinfo
from names_mngmnt import names_mngmnt
from queries_mngmnt import queries_mngmnt
from show_info import show_info


def type_watch(source, value):
    return f"type({source})", type(value)


snoop.install(watch_extras=[type_watch])


@click.command()
@click.argument("keywords", nargs=-1)
@click.option(
    "-q", "--queries", multiple=True, is_flag=False, flag_value="query", default=[]
)
@click.option(
    "-i", "--ids", multiple=True, is_flag=False, flag_value="id", default=[], type=int
)
@click.option(
    "-n", "--names", multiple=True, is_flag=False, flag_value="query", default=[]
)
@click.option("--req / --no-req", default=False)
@snoop
def get_query(keywords, queries, ids, names, req):
    """
    Because we want to deal with complex queries, we'll define that we can receive,
    in the same query, an indefinite number of keywords, queries for natural:
    language search, several id's and names. This module will receive the information
    and send output to different functions.
    """
    cwd = os.getcwd()
    data = f"{cwd}/data_files"

    keys = kwd_mngmnt(keywords)

    if queries != ():
        queries_mngmnt(queries)

    if ids != ():
        ids_mngmnt(ids)

    names_mngmnt(names)

    filelst = os.listdir(os.getcwd())
    if "qlst.bin" or "klst.bin" or "ilst.bin" or "nlst.bin" in filelst:
        checkinfo()
        aggregate_info()
        srch_allinfo()
        show_info(req="no")
        if req:
            show_info(req="yes")

    for i in [f"/usr/bin/trash-put {data}/*", f"/usr/bin/trash-put {cwd}/*.bin"]:
        subprocess.run(i, shell=True)


if __name__ == "__main__":
    get_query()
